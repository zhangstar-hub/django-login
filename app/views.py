# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def home(request):
    return render(request, "home.html")


def signup(request):
    print(request.user.username)
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {'form': form})
