from django.urls import path
from task2.views import index, Index2

urlpatterns = [
    path('', index, name='index'),
    path('class/', Index2.as_view(), name='index2'),
]
