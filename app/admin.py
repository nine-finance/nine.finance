from django.contrib import admin
from .models import timeline
from .models import BackgroundMedia

# Register your models here.
admin.site.register(timeline)
admin.site.register(BackgroundMedia)
