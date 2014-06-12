from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters

from models import Dokarrs
from serializer import DokarrsSerializer, DokarrsFilter

class DokarrsViewSet(viewsets.ModelViewSet):

    queryset = Dokarrs.objects.using('dokarrs').all()
    serializer_class = DokarrsSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.SearchFilter,)
    filter_class = DokarrsFilter
    search_fields =('genus', 'species', 'common_name', 'county','local','obsvr',
                    'month','year','class_field','day','remarks','citatin','family',
                    'obsnum',)