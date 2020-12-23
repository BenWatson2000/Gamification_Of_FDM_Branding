from django.contrib import admin
from .models import AdminAccount, Score, GameQuestion

# Register your models here.

admin.site.register(AdminAccount)
admin.site.register(Score)
admin.site.register(GameQuestion)

