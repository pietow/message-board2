from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Post

class HomePageView(ListView):
     model = Post
     template_name = "home.html"


# class HomePageView(TemplateView):
#     template_name = "home.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['post_list'] = Post.objects.all()
#         return context

