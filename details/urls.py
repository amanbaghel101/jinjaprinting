from details.views import *
from django.urls import path
app_name='anyname'

urlpatterns = [
    path('simple/',simple,name='simple'),
    path('html/',html,name='html'),
    path('jinjaprinting/',jinjaprinting,name='jinjaprinting'),
]
