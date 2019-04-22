from django.contrib import admin
from .models import SmartphoneReviews 
admin.site.register(SmartphoneReviews)
from .models import SmartwatchReviews 
admin.site.register(SmartwatchReviews)
from .models import TabletReviews 
admin.site.register(TabletReviews)
from .models import Product
admin.site.register(Product)
from .models import NewsArticle
admin.site.register(NewsArticle)
# Register your models here.
