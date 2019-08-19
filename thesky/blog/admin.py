from django.contrib import admin
from.models import POST,comment,Project
from .form import commentform
class POSTAdmin(admin.ModelAdmin):
    list_display = ["__str__","post_date","post_update"]

    class Meta:
        model=POST
class commentAdmin(admin.ModelAdmin):
    list_display = ["__str__","comment_date"]
    form = commentform
    #class Meta:
        #model=comment
admin.site.register(POST,POSTAdmin)
admin.site.register(comment,commentAdmin)
admin.site.register(Project)