from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from iapi import views


router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'skill_tags', views.SkillTagViewSet)
router.register(r'project_categories', views.ProjectCategoryViewSet)
router.register(r'project_tasks', views.ProjectTaskViewSet)
router.urls.append(url(r'^user', views.user))
router.urls.append(url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')))

#todo api token urls
router.urls.append(url(r'^token', obtain_auth_token, name='api-token'))



