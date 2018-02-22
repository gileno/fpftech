import json

from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.contrib.auth import authenticate
from django.views.decorators import csrf

from rest_framework.authtoken.models import Token


@csrf.csrf_exempt
def obtain_token(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request=request, username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            data = json.dumps({'token': token.key})
            return HttpResponse(data, content_type='application/json')
        return HttpResponseBadRequest()
    return HttpResponseNotAllowed(permitted_methods=['POST'])
