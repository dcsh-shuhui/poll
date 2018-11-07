from django.shortcuts import render, render_to_response
from django.views.generic import ListView
from .models import *

## Create your views here.
## 投票主題列表
class PollList(ListView):
    model = Poll
