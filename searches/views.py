from django.shortcuts import render

# Create your views here.
from blog.models import BlogPost
from .models import SearchModel


def search_view(request):
    query = request.GET.get('q', None)
    context = {'query': query}
    user = None
    if request.user.is_authenticated:
        user = request.user
    if query is not None:
        SearchModel.objects.create(user=user, query=query) # Save the query every single time
        blog_list = BlogPost.objects.search(query=query)
        context['blog_list'] = blog_list
    return render(request,'searches/view.html',context)