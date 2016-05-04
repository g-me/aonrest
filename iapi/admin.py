from django.contrib import admin

# Register your models here.
from iapi.models import Project, SkillTag, ProjectTask, ProjectCategory

admin.site.register(Project)
admin.site.register(SkillTag)
admin.site.register(ProjectCategory)
admin.site.register(ProjectTask)