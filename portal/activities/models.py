from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from members.models import skill, portal


LEVELS = ( ( 'B', 'Beginner'), ('N','Novice'), ('S','Social'), ('E','Expert') )
DETAIL_TYPES = ( ( 'O', 'Overview'), ('D','Description'), ('C','Course Details'), ('T','Timeline'), ('P','Contact Details') )

class details(models.Model):
    type =  models.CharField(max_length=1, choices=DETAIL_TYPES, default='O')
    class Meta:
        verbose_name_plural = "Details"
        verbose_name = "Detail"

class workshop(models.Model):
    name = models.CharField(max_length=15,null=True)
    poster = models.ImageField(default='')
    link = models.URLField(max_length=100,verbose_name='Workshop URL', null=True)
    level = models.CharField(max_length=1, choices=LEVELS, default='B')
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    skills = models.ManyToManyField(skill,related_name='skills', blank=True)
    organizers = models.ManyToManyField(User,related_name='organizers', blank=True)
    seats = models.IntegerField(null=True, blank=True)
    fee = models.IntegerField(null=True, blank=True)
    details = models.ManyToManyField(details,related_name='details', through='workshop_details')

    class Meta:
        verbose_name_plural = "Workshops"
        verbose_name = "Workshop"

    def __str__(self):
        return self.name


class project(models.Model):
    name = models.CharField(max_length=15,null=True)
    members = models.ManyToManyField(User,blank=True)
    cover = models.ImageField(default='')
    skills = models.ManyToManyField(skill,related_name='project_skills', blank=True)
    details = models.ManyToManyField(details,related_name='project_details', through='project_details')
    links = models.ManyToManyField(portal,related_name='project_links', through='project_links')

    class Meta:
        verbose_name_plural = "Projects"
        verbose_name = "Project"

    def __str__(self):
        return self.name


class project_links(models.Model):
    portal = models.ForeignKey(portal, on_delete=models.CASCADE, related_name='project_links_portal',verbose_name='Portal Name')
    links = models.URLField(max_length=100,verbose_name='Project Page URL')
    project = models.ForeignKey(project, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Project Profile Links"
        verbose_name = "Project Profile Link"

class project_details(models.Model):
    detail = models.ForeignKey(details, on_delete=models.CASCADE, related_name='project_details_detail',verbose_name='Detail Type')
    project = models.ForeignKey(project, on_delete=models.CASCADE, related_name='project_details_project', verbose_name='Project Name')
    title = models.CharField(max_length=15,null=True)
    content = RichTextField(max_length=500, null=True)

    class Meta:
        verbose_name_plural = "Details about Project"
        verbose_name = "Detail about Project"

class workshop_details(models.Model):
    detail = models.ForeignKey(details, on_delete=models.CASCADE, verbose_name='Detail Type')
    workshop = models.ForeignKey(workshop, on_delete=models.CASCADE, verbose_name='Workshop Name')
    title = models.CharField(max_length=15,null=True)
    content = RichTextField(max_length=500, null=True)

    class Meta:
        verbose_name_plural = "Details about Workshop"
        verbose_name = "Detail about Workshop"