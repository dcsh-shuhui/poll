from django.shortcuts import render, render_to_response
from django.views.generic import ListView, DetailView, RedirectView
from .models import *

## Create your views here.
## 投票主題列表
class PollList(ListView):
    model = Poll


## 投票主題檢視
class PollDetail(DetailView):
    model = Poll
    # 取得額外資料供頁面範本顯示
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        options = Option.objects.filter(poll_id=self.kwargs['pk'])
        context['options'] = options
        return context

class PollVote(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        option = Option.objects.get(id=self.kwargs['pk'])
        option.count += 1
        option.save()
        return "/poll/" + str(option.poll_id) + '/'