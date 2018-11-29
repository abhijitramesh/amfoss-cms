from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from status.models import thread


ROLES = (
    ('MN','Mentor'),
    ('Alumini', (
            ('AL', 'Alumini'),
            ('AM', 'Alumini Mentors'),
        )
    ),
    ('Students', (
            ('SM', 'Student Mentor'),
            ('SL', 'Student Member'),
        )
    ),
    ('UN', 'Unknown'),
)

SKILL_TYPES = ( ( 'T', 'Technical'), ('A','Arts'), ('S','Social'), ('P','Sports'), ('O','Others') )


class skill(models.Model):
    name = models.CharField(max_length=25)
    type = models.CharField(choices=SKILL_TYPES,default='O',max_length=1)

    def __str__(self):
        return self.name

class portal(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class organization(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class profile(models.Model):
    def get_dp_path(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return 'static/uploads/images/dp/' + filename

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User', help_text='Select User whose profile is being created')
    email = models.EmailField(max_length=254, null=True)
    phone = models.CharField(max_length=12, null=True)
    first_name = models.CharField(max_length=25, null=True)
    last_name = models.CharField(max_length=25, null=True)
    roll_number = models.CharField(max_length=25,null=True, blank=True)
    role = models.CharField( choices=ROLES, default='SL', max_length=2, verbose_name='Role')
    batch = models.IntegerField(null=True, help_text='Year of Admission', blank=True)
    avatar = models.ImageField(default='',verbose_name='Profile Picture', upload_to=get_dp_path)
    location = models.CharField(max_length=200, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    bio = RichTextField(max_length=300, null=True, blank=True)
    interests = models.ManyToManyField(skill,related_name='interests', blank=True)
    expertise = models.ManyToManyField(skill,related_name='expertise', blank=True)
    typing_speed = models.IntegerField(null=True, blank=True)
    experiances = models.ManyToManyField(organization,related_name='work_experiances',through='work_experiances',blank=True)
    system_no = models.IntegerField(null=True, blank=True)
    links = models.ManyToManyField(portal, related_name = 'social_links', through='social_profiles')

    class Meta:
        verbose_name_plural = "Profiles"
        verbose_name = "Profile"

    def __str__(self):
        return self.first_name

class social_profiles(models.Model):
    portal = models.ForeignKey(portal, on_delete=models.CASCADE, verbose_name='Portal Name')
    link = models.URLField(max_length=100,verbose_name='Profile URL')
    profile = models.ForeignKey(profile, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Social Profile Links"
        verbose_name = "Social Profile Link"

class work_experiances(models.Model):
    organization = models.ForeignKey(organization, on_delete=models.CASCADE, related_name='organization',verbose_name='Organization')
    profile = models.ForeignKey(profile, on_delete=models.CASCADE,related_name='profile')
    position = models.CharField(max_length=35, null=True)
    description = RichTextField(max_length=300, null=True, blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Work Experiances"
        verbose_name = "Work Experiance"

class attendance(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    session_start = models.DateTimeField()
    session_end = models.DateTimeField()

    class Meta:
        verbose_name_plural = "attendance"
        verbose_name = "attendance"

    def __str__(self):
        return self.member.username

class responsibility(models.Model):
    title = models.CharField(max_length=100)
    about = RichTextField(max_length=500, null=True, blank=True)
    thread = models.OneToOneField(thread, on_delete=models.CASCADE, null=True, blank=True)
    members = models.ManyToManyField(User,blank=True)

    class Meta:
        verbose_name_plural = "Responsibilities"
        verbose_name = "Responsibility"

    def __str__(self):
        return self.title

class team(models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField()
    about = RichTextField(max_length=500, null=True, blank=True)
    thread = models.OneToOneField(thread, on_delete=models.CASCADE, null=True)

    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class mentor_group(models.Model):
    mentor =  models.OneToOneField(User, on_delete=models.CASCADE, related_name='mentor', verbose_name='Mentor Name')
    mentees = models.ManyToManyField(User,related_name='Mentees')

    class Meta:
        verbose_name_plural = "Mentor Groups"
        verbose_name = "Mentor Group"

    def __str__(self):
        return self.mentor.username