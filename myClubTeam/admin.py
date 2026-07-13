from django.contrib import admin
from .models import Team ,Player,Standing,Match
from django.contrib.auth.admin import UserAdmin


# Register your models here.
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Standing)
admin.site.register(Match)
