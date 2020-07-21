from django.shortcuts import render
from django.conf import settings
from django.db import models
from django.utils import timezone


def post_list(request):
    return render(request, 'mainpage/post_list.html', {})

