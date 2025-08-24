from django.contrib import admin
from .models import Expense, Category

# admin.site.register(Expense)
# admin.site.register(Category)

admin.site.site_header = "Expense Tracker"
admin.site.site_title = "Expense Tracker Admin Portal"
admin.site.index_title = "Welcome to the Expense Tracker Admin"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')  


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'category', 'user', 'date')
