from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from members.models import Skill, Portal


LEVELS = ( ( 'B', 'Beginner'), ('N','Novice'), ('S','Social'), ('E','Expert') )
DETAIL_TYPES = ( ( 'O', 'Overview'), ('D','Description'), ('C','Course Details'), ('T','Timeline'), ('P','Contact Details') )


class Detail(models.Model):
    type =  models.CharField(max_length=1, choices=DETAIL_TYPES, default='O')

    class Meta:
        verbose_name_plural = "Details"
        verbose_name = "Detail"


class Workshop(models.Model):
    name = models.CharField(max_length=15, null=True)
    poster = models.ImageField(default='')
    link = models.URLField(max_length=100, verbose_name='Workshop URL', null=True)
    level = models.CharField(max_length=1, choices=LEVELS, default='B')
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    skills = models.ManyToManyField(Skill, related_name='skills', blank=True)
    organizers = models.ManyToManyField(User, related_name='organizers', blank=True)
    seats = models.IntegerField(null=True, blank=True)
    fee = models.IntegerField(null=True, blank=True)
    details = models.ManyToManyField(Detail, related_name='details', through='WorkshopDetail')

    class Meta:
        verbose_name_plural = "Workshops"
        verbose_name = "Workshop"

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=15, null=True)
    members = models.ManyToManyField(User, blank=True)
    cover = models.ImageField(default='')
    skills = models.ManyToManyField(Skill, related_name='ProjectSkills', blank=True)
    details = models.ManyToManyField(Detail, related_name='projectDetails', through='ProjectDetail')
    links = models.ManyToManyField(Portal, related_name='ProjectLinks', through='ProjectLink')

    class Meta:
        verbose_name_plural = "Projects"
        verbose_name = "Project"

    def __str__(self):
        return self.name


class ProjectLink(models.Model):
    portal = models.ForeignKey(Portal, on_delete=models.CASCADE, related_name='project_links_portal', verbose_name='Portal Name')
    links = models.URLField(max_length=100,verbose_name='Project Page URL')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Project Profile Links"
        verbose_name = "Project Profile Link"


class ProjectDetail(models.Model):
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE, related_name='project_details_detail', verbose_name='Detail Type')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_details_project', verbose_name='Project Name')
    title = models.CharField(max_length=15, null=True)
    content = RichTextField(max_length=500, null=True)

    class Meta:
        verbose_name_plural = "Details about Project"
        verbose_name = "Detail about Project"


class WorkshopDetail(models.Model):
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE, verbose_name='Detail Type')
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE, verbose_name='Workshop Name')
    title = models.CharField(max_length=15, null=True)
    content = RichTextField(max_length=500, null=True)

    class Meta:
        verbose_name_plural = "Details about Workshop"
        verbose_name = "Detail about Workshop"

