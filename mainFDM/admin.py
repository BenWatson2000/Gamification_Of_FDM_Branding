from django.contrib import admin
from .models import HelperAccount, Score, GameQuestion

# Register your models here.

admin.site.register(HelperAccount)
admin.site.register(Score)
admin.site.register(GameQuestion)
