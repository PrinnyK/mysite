from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import article

# Create your views here.

class articleListView(ListView):
    model = article
    queryset = article.objects.all()
    template_name = 'blog/list.html'
    ordering = "-date"
    context_object_name = "articles"

class articleDetailView(DetailView):
    model = article
    template_name = "blog/detail.html"
