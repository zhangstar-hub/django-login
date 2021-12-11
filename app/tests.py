# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django import setup
from django.test import TestCase

# Create your tests here.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
setup()

from django.contrib.auth.models import User, Permission, Group
from django.contrib.contenttypes.models import ContentType
from app.models import UrlPermProxy

# User.objects.create_user("zxx", password="zxx")
u = User.objects.get(id=1)
content_type = ContentType.objects.get_for_model(UrlPermProxy, for_concrete_model=False)
permission = Permission.objects.filter(content_type=content_type)
print(permission)
# super_user = Group('super_user')
# perm = Permission.objects.create(
#     codename='view_prize',
#     name="view prize",
#     content_type=content_type
# )

# perm = Permission.objects.get(codename="view_prize")
# u.user_permissions.add(perm)
# print(u.user_permissions.all())
# print(u.has_perm("app.view_prize"))
