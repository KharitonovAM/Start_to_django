from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product

class Command(BaseCommand):
    help = "Добавляем тестовую информацию в базу данных, предварительно удаляем уже имеющуюся в БД информацию"

    def handle(self, *args, **options):

        #Очищаем имеющиеся данные из БД
        Category.objects.all().delete()
        Category.objects.all().delete()

        #загружаем данные из фикстуры
        call_command('loaddata', 'category_fixture.json')
        call_command('loaddata', 'product_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))

