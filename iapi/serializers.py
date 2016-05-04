from django.contrib.auth import get_user_model
from rest_framework import serializers
from iapi.models import Project, ProjectCategory, ProjectTask, SkillTag

User = get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='user-detail', lookup_field=User.USERNAME_FIELD)

    class Meta:
        model = User
        fields = ('id', User.USERNAME_FIELD, 'email', 'is_active', 'url')


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    created_by = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True, lookup_field='username')
    skills = serializers.HyperlinkedRelatedField(view_name='skilltag-detail', many=True, read_only=True,
                                                 lookup_field='slug')

    class Meta:
        model = Project
        fields = ('id','title', 'description', 'slug', 'status', 'url', 'created_at', 'updated_at', 'skills', 'category','task', 'created_by')


class SkillTagSerializer(serializers.HyperlinkedModelSerializer):
    created_by = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True, lookup_field='username')
    url = serializers.HyperlinkedIdentityField(lookup_field='slug', view_name='skilltag-detail')

    class Meta:
        model = SkillTag
        fields = ('id', 'name', 'description', 'url', 'created_by', 'created_at', 'updated_at')


class ProjectCategorySerializer(serializers.HyperlinkedModelSerializer):
    created_by = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True, lookup_field='username')

    class Meta:
        model = ProjectCategory
        fields = ('id', 'name', 'description', 'url', 'created_by', 'created_at', 'updated_at')


class ProjectTaskSerializer(serializers.HyperlinkedModelSerializer):
    created_by = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True, lookup_field='username')

    class Meta:
        model = ProjectTask
        fields = ('id', 'name', 'description', 'url', 'created_by', 'created_at', 'updated_at')
