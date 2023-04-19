from django.urls import path

from . import views


urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('search_tuple', views.search_tuple, name='search'),
    # ex: /polls/5/results/
path('table-scan', views.table_scan, name='show'),

    # ex: /polls/5/vote/

]
