__author__ = 'mstacy'
from rest_framework import serializers
from models import Doe
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

class DoeSerializer(DynamicFieldsModelSerializer, serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Doe
        fields = ('url', 'county', 'site_number', 'dertermination', 'referent', 'agency',)



class DoeFilter(django_filters.FilterSet):
    county = django_filters.CharFilter(lookup_type='icontains')
    site_number = django_filters.CharFilter(lookup_type='icontains')
    dertermination = django_filters.DateFilter(lookup_type='exact')
    min_date = django_filters.DateFilter(name='dertermination', lookup_type='gte')
    max_date = django_filters.DateFilter(name='dertermination', lookup_type='lte')
    referent = django_filters.CharFilter(lookup_type='icontains')
    agency = django_filters.CharFilter(lookup_type='icontains')

    class Meta:
        model = Doe
        fields = ['county', 'site_number', 'dertermination', 'referent', 'agency']

