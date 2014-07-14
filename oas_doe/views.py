from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters

from models import Doe
from serializer import DoeSerializer, DoeFilter


class DoeViewSet(viewsets.ModelViewSet):
    queryset = Doe.objects.using('doe').all()
    serializer_class = DoeSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    filter_class = DoeFilter
    search_fields = ('county', 'site_number', 'referent', 'agency',)
    ordering_fields = ('county', 'site_number', 'dertermination', 'referent', 'agency')