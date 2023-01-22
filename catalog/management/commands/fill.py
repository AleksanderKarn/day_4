from django.core.management import BaseCommand

from catalog.models import Category

class Command(BaseCommand):

    def delete_everything(self):
        Category.objects.all().delete()

    def handle(self, *args, **options):
        categories = [
            {'category_name': 'Фрукты', 'description': 'Вкусно и полезно', 'image': 'img/products/iphone_1.jpg'},
            #{'category_name': 'Овощи', 'description': 'Содержат клетчатку'},
            #{'category_name': 'Ягоды', 'description': 'Богаты витаминами'},
            #{'category_name': 'Орехи', 'description': 'Полезны для мозга'},
        ]

        categories_list = []

        for item in categories:
            categories_list.append(Category(**item))
       # self.delete_everything() # очичает таблицу перед заполнением
        Category.objects.bulk_create(categories_list)

