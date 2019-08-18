from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import BlogPostModelForm, BlogPostForm

# Create your views here.
from .models import BlogPost

# create_page = Needs a form
# detail_page = Needs id i.e object
# delete_page = Needs id i.e object
# list_page = query_Set
# update_page = needs form and id, id is passed to form to update it


#@login_required()
@staff_member_required
def blog_post_create_page(request, *args, **kwargs):
    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    template_name = 'blog/form.html'
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user # ***Complete user association to a blog is happening here
        obj.save()
        form = BlogPostModelForm()

    context = {'form': form}
    return render(request, template_name, context)


@staff_member_required
def blog_post_detail_page(request, slug):

    object_name = get_object_or_404(BlogPost, slug=slug)
    context = {'object': object_name}
    template_name = 'blog/detail.html'

    return render(request, template_name, context)

@staff_member_required
def blog_post_delete_page(request, slug):

    template_name = 'blog/delete.html'

    object_name = get_object_or_404(BlogPost, slug=slug)

    if request.method == 'POST':
        object_name.delete()
        return redirect('/blog')
    context = {'object': object_name}

    return render(request, template_name, context)


def blog_post_list_page(request, *args, **kwargs):

    #query_set = BlogPost.objects.all()
    query_set = BlogPost.objects.all().published()
    print(query_set)
    context = {'object_list': query_set}
    template_name = 'blog/list.html'

    return render(request, template_name, context)


@staff_member_required
def blog_post_update_page(request, slug):

    template_name = 'blog/form.html'
    obj = get_object_or_404(BlogPost,slug=slug)
    title = 'Update ' + str(obj.title)
    form = BlogPostModelForm(request.POST or None,instance=obj)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user # ***Complete user association to a blog is happening here
        obj.save()
        form = BlogPostModelForm()

    context = {'form': form,'title':title}
    return render(request, template_name, context)