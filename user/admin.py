from django.contrib import admin
from .models import Card,Admin,Driver,Owner,CustomUser


admin.site.register(Card)
admin.site.register(Admin)
admin.site.register(Driver)
admin.site.register(Owner)
admin.site.register(CustomUser)
