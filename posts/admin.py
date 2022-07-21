from django.contrib import admin
from .models import aparteman,vilae,zamin,aparteman_images,zamin_image,vilae_image,IPAddressApa,IPAddressVilla
# Register your models here.


admin.site.register(aparteman)
admin.site.register(vilae)
admin.site.register(zamin)
admin.site.register(aparteman_images)
admin.site.register(zamin_image)
admin.site.register(vilae_image)
admin.site.register(IPAddressApa)
admin.site.register(IPAddressVilla)