from django.shortcuts import render
from .models import *
from django.urls import reverse
from django.views.generic import UpdateView


class UpdatePostView(UpdateView):
    model = Post
    fields = ['name', 'surename', 'group']
    template_name = 'update.html'

    def get_success_url(self) -> str:
        return reverse('home')
    
def home(request):
    return render(request, 'index.html')
