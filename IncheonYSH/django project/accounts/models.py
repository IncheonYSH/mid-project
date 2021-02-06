from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    year = models.CharField('year', max_length=6)
    day = models.CharField('day', max_length=6)
    month_select = (
        ("01", "1"),
        ("02", "2"),
        ("03", "3"),
        ("04", "4"),
        ("05", "5"),
        ("06", "6"),
        ("07", "7"),
        ("08", "8"),
        ("09", "9"),
        ("10", "10"),
        ("11", "11"),
        ("12", "12")
    )
    month = models.CharField('month', max_length=6, choices=month_select)
    sex_select = (
        ("M", "남자"),
        ("F", "여자")
    )
    sex = models.CharField('sex', max_length=6, choices=sex_select)

    def __str__(self):
        return self.year

"""
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, user_pk=instance.id)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
"""