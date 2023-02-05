from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest, JsonResponse
from django.views.decorators.http import require_GET
from django.utils import timezone
import json
from products import constants
from products import private


@require_GET
def get_products(request):
    limit_str = request.GET.get('limit')
    offset_str = request.GET.get('offset')
    filters_str = request.GET.get('filters')

    # Check offset and limit
    if not limit_str or not offset_str:
        return HttpResponseBadRequest('Data not valid!!')
    
    # Check limit and its validation
    if not limit_str.isdigit() or not offset_str.isdigit():
        return HttpResponseBadRequest('Data not valid!!')
    
    try:
        filters_dict = json.loads(filters_str)
    except Exception:
        return HttpResponseBadRequest('Filters are not in correct format')

    limit = int(limit_str)
    offset = int(offset_str)

    if limit > constants.MAX_PRODUCTS_PER_PAGE:
        return HttpResponseBadRequest('Product per page limit exceeded!!')

    products = private.get_paginated_products(limit, offset, filters_dict)

    return JsonResponse(
        {
            'products': products,
            'meta': {
                'limit': limit,
                'offset': offset
            }
        }
    )