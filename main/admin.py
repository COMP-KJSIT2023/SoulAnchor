from django.contrib import admin
from .models import Survey_filled, Question, Option, Answer

# Register your models here.
admin.site.register(Survey_filled)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Answer)