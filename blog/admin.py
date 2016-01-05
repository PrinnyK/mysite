from django.contrib import admin
from .models import article, category
# Register your models here.

class articleAdmin(admin.ModelAdmin):
	list_display = ('title', 'date', 'category')
	fields = (
		'title',
		'content',
		'category'
	)
	search_fields = ('title',)
	ordering = ('-date',)
	list_per_page = 60

class categoryAdmin(admin.ModelAdmin):
	list_display = ('title',)

admin.site.register(article, articleAdmin)
admin.site.register(category, categoryAdmin)
