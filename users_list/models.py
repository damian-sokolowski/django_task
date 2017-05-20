# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

import random


def get_random_number():
    return random.randint(1, 100)


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile',)
    birthday = models.DateField(blank=True, null=True,)
    random_number = models.IntegerField(default=get_random_number,)
