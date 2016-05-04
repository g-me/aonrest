from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

# project status code
STATUS_OPEN = 100
STATUS_DONE = 101
STATUS_CLOSED = 102


class SkillTag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, force_insert=False, force_update=False, using=None,update_fields=None):
        self.slug = slugify(self.name)
        super(SkillTag, self).save(force_insert, force_update, using, update_fields)


    def __str__(self):
        return self.name


class ProjectTask(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, blank=True)
    skill_tags = models.ManyToManyField(SkillTag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, force_insert=False, force_update=False, using=None,update_fields=None):
        self.slug = slugify(self.name)
        super(ProjectTask, self).save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name


class ProjectCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, blank=True)
    tasks = models.ManyToManyField(ProjectTask, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.name)
        super(ProjectCategory, self).save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "RequestCategory"
        verbose_name_plural = "Request Categories"


class Project(models.Model):
    PROJECT_STATUS = (
        (STATUS_OPEN, _('Open')),
        (STATUS_DONE, _('Done')),
        (STATUS_CLOSED, _('Closed'))
    )
    title = models.CharField(max_length=200)
    category = models.ForeignKey(ProjectCategory, blank=True, null=True)
    task = models.ForeignKey(ProjectTask, blank=True, null=True)        #todo:validation task must be in project categry
    description = models.TextField(blank=True)
    status = models.SmallIntegerField(choices=PROJECT_STATUS, blank=True, default=STATUS_OPEN)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    created_by = models.ForeignKey(User, related_name='requested_by')
    skills = models.ManyToManyField(SkillTag, blank=True, related_name='collaborators')
    collaborators = models.ManyToManyField(User, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Project, self).save(force_insert, force_update, using, update_fields)

    def is_published(self):
        return self.status != STATUS_CLOSED
