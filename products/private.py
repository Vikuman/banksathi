from products import constants
from products import models

def get_paginated_products(limit, offset, filters_dict):
    brands = [brand.lower() for brand in filters_dict.get('brands', [])]
    colors = [color.lower() for color in filters_dict.get('colors', [])]
    low_price = filters_dict.get('low_price', 0)
    high_price = filters_dict.get('high_price')
    discount = filters_dict.get('discount', 0)
    print(brands)
    print(colors)
    qs = models.Product.objects.filter(
        price__gte=low_price,
        discount__gte=discount
    )

    if colors:
        qs = qs.filter(color__in=colors)
    if brands:
        qs = qs.filter(brand__in=brands)
    if high_price:
        qs = qs.filter(price__lte=high_price)
    return list(
        qs[offset: limit+offset].values(
            'brand',
            'description',
            'img_url',
            'rating',
            'price',
            'actual_price',
            'discount'
        )
    )



