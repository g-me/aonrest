from django.contrib.auth import get_user_model
import django_filters
from iapi.models import Project

User = get_user_model()


class NullFilter(django_filters.BooleanFilter):
    def filter(self, qs, value):
        if value is not None:
            return qs.filter(**{'%s__isnull' % self.name: value})
        return qs


class ProjectFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = ('created_by', 'status','skills','category',)

