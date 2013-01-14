from django.http import HttpResponse
from django.views.generic import View

class MyView(View):
    def post(request, *args, **kwargs):
        return HttpResponse('post!')
