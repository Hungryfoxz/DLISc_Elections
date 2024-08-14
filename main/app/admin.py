from django.contrib import admin
from .models import Register, Voted, Positions, Candidate
from django.contrib import admin

admin.site.index_template = 'admin/index.html'
admin.site.base_template = 'admin/base.html'


# Register your models here.
admin.site.register(Register)
admin.site.register(Voted)
admin.site.register(Positions)
admin.site.register(Candidate)