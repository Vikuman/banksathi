# Starting the Project!

Install all the dependencies
`pip install requirements.txt`

Create Database Model
`python manage.py migrate `

Polpulate data from dummy data
`python manage.py shell < products/data.py`

Runserver
`python manage.py runserver`

API:
```
GET: /api/v1/products/items
params: 
limit: integer
offset: integer
filters: dict(with all the filters)
	eg.: {
			"colors": ["blue", "yello"],
			"brands": ["roadster", "adidas"],
			"low_price": 120,
			"high_price": 300,
			"discount": 56
		}
```
