__author__ = 'mstacy'
from rest_framework import serializers
from models import Dokarrs
import django_filters


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        fields = self.context['request'].QUERY_PARAMS.get('fields')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class DokarrsSerializer(DynamicFieldsModelSerializer, serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Dokarrs
        fields = ('url', 'obsnum', 'class_field', 'family', 'genus',
                  'species', 'common_name', 'county', 'local', 'obsvr',
                  'day', 'month', 'year', 'number', 'habitat', 'remarks',
                  'museum', 'citatin', 'timestamp')


class DokarrsFilter(django_filters.FilterSet):
    genus = django_filters.CharFilter(lookup_type='icontains')
    species = django_filters.CharFilter(lookup_type='icontains')
    common_name = django_filters.CharFilter(lookup_type='icontains')
    county = django_filters.CharFilter(lookup_type='icontains')
    local = django_filters.CharFilter(lookup_type='icontains')
    obsvr = django_filters.CharFilter(lookup_type='icontains')
    month = django_filters.CharFilter(lookup_type='icontains')
    year = django_filters.CharFilter(lookup_type='icontains')
    class_field = django_filters.CharFilter(lookup_type='icontains')
    day = django_filters.CharFilter(lookup_type='icontains')
    remarks = django_filters.CharFilter(lookup_type='icontains')
    citatin = django_filters.CharFilter(lookup_type='icontains')
    family = django_filters.CharFilter(lookup_type='icontains')
    obsnum = django_filters.CharFilter(lookup_type='icontains')
    min_date = django_filters.DateFilter(name='timestamp', lookup_type='gte')
    max_date = django_filters.DateFilter(name='timestamp', lookup_type='lte')

    class Meta:
        model = Dokarrs
        fields = ['genus', 'species', 'common_name', 'county', 'local', 'obsvr',
                  'month', 'year', 'class_field', 'day', 'remarks', 'citatin', 'family',
                  'obsnum']

