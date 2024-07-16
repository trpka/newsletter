from django.contrib import admin
from .models import User, Organization, Company

admin.site.register(User)
admin.site.register(Organization)
admin.site.register(Company)
