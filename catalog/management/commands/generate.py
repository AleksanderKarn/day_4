from django.core.management import BaseCommand

from catalog.models import Product


def deleted_everything():
    Product.objects.all().delete()


class Command(BaseCommand):

    def delete_everything(self):
        Product.objects.all().delete()

    def handle(self, *args, **options):
        categories = [
            {'name_product': 'iPhone', 'image': '/img/products/iphone_1.jpg', 'category_name': 'Телефоны', 'description': 'Современный гаджет со всевозможными наворотами', 'unit_price': 99.99},
            {'name_product': 'iMac', 'image': '/img/products/imac_1.jpg', 'category_name': 'Ноутбук', 'description': 'Топ для разработки', 'unit_price': 289.99},
            {'name_product': 'HP', 'image': '/img/products/hp_1.jpg', 'category_name': 'Ноутбук', 'description': 'ну МАААМ ну правдо для учебы', 'unit_price': 124.99},
            {'name_product': 'Canon EOS', 'image': '/img/products/canon_eos_5d_1.jpg', 'category_name': 'Фотоаппарат', 'description': 'Сданным устройством ваши дикпики станут еще более выразитльные и живописные', 'unit_price': 149.99},

        ]
        product_list = []
        for item in categories:
            product_list.append(Product(**item))
        #deleted_everything()  # очичает таблицу перед заполнением
        Product.objects.bulk_create(product_list)

