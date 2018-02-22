from rest_framework.authtoken.models import Token


def authtoken_middleware(get_response):

    def middleware(request):

        if not request.user.is_authenticated:
            auth_header = request.META.get('Authorization', None)
            if auth_header:
                auth_header = auth_header.split()
                try:
                    token = Token.objects.get(key=auth_header[1])
                    request.user = token.user
                except Token.DoesNotExist:
                    pass

        response = get_response(request)

        return response

    return middleware
