# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class UrlPerm(models.Model):
    perm_list = models.TextField(default="[]", blank=True)


class UrlPermProxy(UrlPerm):
    class Meta:
        proxy = True
        permissions = [("view_test_tools", "view test tool")]
