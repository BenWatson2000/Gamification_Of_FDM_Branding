from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import HelperAccount, Score, GameQuestion, HelperProfile

# Register your models here.

# admin.site.register(HelperAccount)
admin.site.register(HelperProfile)
admin.site.register(Score)
admin.site.register(GameQuestion)