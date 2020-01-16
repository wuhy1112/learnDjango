from django.http import HttpResponse
from django.views import View


class ProjectsView(View):
    def get(self, request):
        return HttpResponse("get请求")

    def post(self, request):
        return HttpResponse("post请求")

    def put(self, request):
        return HttpResponse("put请求")
