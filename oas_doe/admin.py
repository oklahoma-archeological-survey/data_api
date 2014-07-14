from django.contrib import admin

# Register your models here.
from django.contrib import admin
from models import Doe
from guardian.admin import GuardedModelAdmin

# Register your models here.
class MultiDBModelAdmin(GuardedModelAdmin):#admin.ModelAdmin):
    # A handy constant for the name of the alternate database.

    using = 'doe'

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'other' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'other' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        return super(MultiDBModelAdmin, self).get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        return super(MultiDBModelAdmin, self).formfield_for_foreignkey(db_field, request=request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        return super(MultiDBModelAdmin, self).formfield_for_manytomany(db_field, request=request, using=self.using, **kwargs)

class DoeAdmin(MultiDBModelAdmin):
    list_display = ('county', 'site_number', 'dertermination', 'referent', 'agency')
    #ordering = ('-timestamp',)
    #date_hierarchy = 'timestamp'

admin.site.register(Doe, DoeAdmin)