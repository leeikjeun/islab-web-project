from django.contrib import admin
from .models import Profile, UnknowNameBoard, ProffessorData, Proffessorcontent
# Register your models here.

admin.site.register(Profile)
admin.site.register(UnknowNameBoard)
admin.site.register(ProffessorData)
admin.site.register(Proffessorcontent)
