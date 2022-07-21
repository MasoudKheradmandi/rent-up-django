from posts.models import IPAddressApa,IPAddressVilla

class SaveIPAddressSimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        

        try:
            ip_address = IPAddressApa.objects.get(ip_address=ip)
        except IPAddressApa.DoesNotExist:
            ip_address = IPAddressApa(ip_address=ip)
            ip_address.save()

        request.user.ip_address = ip_address

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
    
class SaveIPAddressVillaSimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        

        try:
            ip_address = IPAddressVilla.objects.get(ip_address=ip)
        except IPAddressVilla.DoesNotExist:
            ip_address = IPAddressVilla(ip_address=ip)
            ip_address.save()

        request.user.ip_address = ip_address

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response