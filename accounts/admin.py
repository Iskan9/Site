from django.contrib import admin

# Register your models here.

# без этого, не будут работать созданные нами модели, в models
from .models import *  # импортируем все

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tag)



