from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters

from models import Dokarrs
from serializer import DokarrsSerializer, DokarrsFilter
from rest_framework.renderers import JSONRenderer, YAMLRenderer, JSONPRenderer, BrowsableAPIRenderer,XMLRenderer


class DokarrsViewSet(viewsets.ModelViewSet):
    #renderer_classes = (BrowsableAPIRenderer, JSONRenderer, JSONPRenderer, YAMLRenderer)
    queryset = Dokarrs.objects.using('dokarrs').all()
    serializer_class = DokarrsSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,)
    filter_class = DokarrsFilter
    search_fields = ('genus', 'species', 'common_name', 'county', 'local', 'obsvr',
                     'month', 'year', 'class_field', 'day', 'remarks', 'citatin', 'family',
                     'obsnum', 'number', 'habitat', 'museum',)
