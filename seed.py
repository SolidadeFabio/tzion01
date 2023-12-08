import os
import django
import random
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from project.models import Product, Supplier

fake = Faker()

for _ in  range(100):
    supplier = Supplier(
        cnpj=fake.bothify(text='##############'),
        name=fake.company()
    )
    supplier.save()
    pass

suppliers = Supplier.objects.all()

for _ in range(10000): 
    product = Product(
        name=fake.company(),
        cas_number=fake.bothify(text='###-###-#'),
        purch_price=random.uniform(100.0, 1000.0),
        purch_cod=fake.bothify(text='CODE###'),
        description=fake.text(),
        brand=fake.company_suffix(),
        sell_cod=fake.bothify(text='SELL###'),
        sell_price=random.uniform(1000.0, 2000.0),
        product_type=random.choice(['NATIONAL', 'IMPORTED']),
        quantity=random.randint(1, 100),
        supplier=random.choice(suppliers)
    )
    product.save()
