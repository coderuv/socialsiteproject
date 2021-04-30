from django.contrib import admin
from .models import Contact
from .models import user_post
from .models import userconnection
from .models import followcount
# Register your models here.
admin.site.register(Contact)
admin.site.register(user_post)
admin.site.register(userconnection)
admin.site.register(followcount)
