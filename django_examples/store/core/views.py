from django.shortcuts import render
from django.http import HttpResponse


class IndexView(object):

    def __call__(self, request):
        return HttpResponse('Index View')


index = IndexView()
