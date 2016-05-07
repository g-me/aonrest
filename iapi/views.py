from django.contrib.auth import get_user_model
from rest_framework import authentication, permissions, viewsets, filters
from rest_framework.decorators import list_route, detail_route, api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from iapi.forms import ProjectFilter
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

    filter_backends = (filters.SearchFilter,
                       filters.OrderingFilter,
                       filters.DjangoFilterBackend
                       )


class ProjectViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = Project.objects.order_by('created_at')
    serializer_class = ProjectSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    filter_class = ProjectFilter
    search_fields = ('title', 'description')
    ordering_fields = ('created_at',)


class SkillTagViewSet(DefaultsMixin, viewsets.ModelViewSet):
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    queryset = SkillTag.objects.order_by('slug')
    serializer_class = SkillTagSerializer
    search_fields = ('name', 'description')
    ordering_fields = ('created_at',)


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
    search_fields = ('username', 'first_name')
    ordering_fields = ('created_at',)

    @list_route(permission_classes=[permissions.IsAuthenticated],
                authentication_classes=[authentication.BasicAuthentication])
    def proj(self, request):
        user = request.user
        projects = Project.objects.filter(created_by=user)
        serializer = ProjectSerializer(projects, many=True, context={'request': request})
        return Response(serializer.data)

    @detail_route(permission_classes=[permissions.IsAuthenticated],
                  authentication_classes=[authentication.BasicAuthentication])
    def projects(self, request, username=None):
        user = self.get_object()
        projects = Project.objects.filter(created_by=user)
        serializer = ProjectSerializer(projects, many=True, context={'request': request})
        return Response(serializer.data)


# - GET api/user

@api_view()
@permission_classes([permissions.IsAuthenticated, ])
@authentication_classes([authentication.TokenAuthentication, ])
def user(request):
    u = request.user
    serializer = UserSerializer(u, context={'request': request})
    return Response(serializer.data)
