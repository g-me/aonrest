from django.contrib.auth import get_user_model
from rest_framework import authentication, permissions, viewsets
from iapi.serializers import ProjectSerializer, SkillTagSerializer, ProjectCategorySerializer, ProjectTaskSerializer, \
    UserSerializer
from iapi.models import Project, SkillTag, ProjectTask, ProjectCategory

User = get_user_model()


class DefaultsMixin(object):
    """ Default settings for view authentication, permissions,
        filtering and pagination."""
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class ProjectViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = Project.objects.order_by('created_at')
    serializer_class = ProjectSerializer


class SkillTagViewSet(DefaultsMixin, viewsets.ModelViewSet):
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    queryset = SkillTag.objects.order_by('slug')
    serializer_class = SkillTagSerializer


class ProjectCategoryViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = ProjectCategory.objects.order_by('created_at')
    serializer_class = ProjectCategorySerializer


class ProjectTaskViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = ProjectTask.objects.order_by('created_at')
    serializer_class = ProjectTaskSerializer


class UserViewSet(DefaultsMixin, viewsets.ModelViewSet):
    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer
