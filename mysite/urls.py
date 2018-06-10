from django.http import HttpResponse
from django.contrib import admin
from django.urls import include, path

def hello_world(request):
    return HttpResponse('astf')

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('', hello_world),
]