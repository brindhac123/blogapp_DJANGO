from typing import Any
from blog.models import Category
from django.core.management.base import BaseCommand # type: ignore
from django.utils.text import slugify

class Command(BaseCommand):
    help="This commands inserts post data"

    def handle(self, *args:Any, **options: Any):
        Category.objects.all().delete()
        #delete all existing data
        #Post.objects.all().delete()


        categories = ['Sports', 'Technology', 'Science', 'Art', 'Food']
      

        for category_name in categories:
            Category.objects.create(name = category_name)
            
        self.stdout.write(self.style.SUCCESS("Complete Inserting Data"))







        

