from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import article
import img_sp
# Create your views here.

class articleListView(ListView):
    model = article
    queryset = article.objects.all()
    template_name = 'blog/list.html'
    ordering = "-date"
    context_object_name = "articles"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(articleListView, self).get_context_data(**kwargs)
        context['img'] = img_sp.GetLink(img_sp.GetPage())
        return context

class articleDetailView(DetailView):
    model = article
    template_name = "blog/detail.html"
