from rest_framework.routers import DefaultRouter
from iapi import views

router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'skill_tags', views.SkillTagViewSet)
router.register(r'project_categories', views.ProjectCategoryViewSet)
router.register(r'project_tasks', views.ProjectTaskViewSet)
