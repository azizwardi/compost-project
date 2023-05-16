from django.contrib import admin
from .models import *

admin.site.register(project)
admin.site.register(client)
admin.site.register(nodes)
admin.site.register(Post)