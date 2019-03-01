from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.
class OrderLineAdminInline(admin.TabularInline): #TabularInline subclass defines the template used to render the Order in the admin interface. StackedInline is another option
    model = OrderLineItem
    
# The admin interface has the ability to edit more than one model on a single page. This is known as inlines
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline,)
    
# Register the model with the admin site so you can edit them if necessary
admin.site.register(Order, OrderAdmin)