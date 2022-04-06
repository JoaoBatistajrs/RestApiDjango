from django.contrib import admin
from financepy.models import Register

class Registers(admin.ModelAdmin):
  list_display = ('id','description', 'price', 'category')
  list_display_links = ('id','description')
  search_fields = ['description']

admin.site.register(Register, Registers)