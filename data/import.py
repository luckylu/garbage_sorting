import csv
from api.models import Garbage
from api.models import Category
categories = [(1, '可回收垃圾'), (2, '有害垃圾'), (4, '湿垃圾'), (8, '干垃圾'), (16, '大件垃圾')]

for category in categories:
    Category.objects.get_or_create(id=category[0], name=category[1])
with open('data/garbage.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = Garbage.objects.get_or_create(
            name=row[0],
            category_id=row[1],
            )


