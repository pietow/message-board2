from django.views.generic import ListView, TemplateView
from .models import Post


class HomePageView(ListView):
    template_name = "home.html"
    model = Post

# class HomePageView(TemplateView):
#     template_name = "home.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['post_list'] = list(Post.objects.all())
#         # context['post_list'].append('Bla2') 
#         return context

