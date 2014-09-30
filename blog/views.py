from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404, get_list_or_404, render_to_response
from django.core.urlresolvers import reverse
from django.views import generic
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.core import serializers
from django.db.models import Max, Min
import json


from blog.models import *

# this is a old and complicated way to serve page
def index(request):
#    latest_post_list = Post.objects.order_by('-published')[:5]  #first 5 items order by published desc
    latest_post_list = Post.objects.all().order_by('-published')
    tags = Tag.objects.all()
    paginator = Paginator(latest_post_list, 10)
    page = request.GET.get('page')
    
    try:
        latest_posts = paginator.page(page)
    except PageNotAnInteger:
        latest_posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        latest_posts = paginator.page(paginator.num_pages)
    
#    template = loader.get_template('blog/index.html')
#    context = RequestContext(request, {
#        'latest_post_list': latest_posts,
#        'tags': tags,
#    })
    return render_to_response('blog/index.html', {
        'latest_posts': latest_posts,
        'tags': tags,})
#    return HttpResponse(template.render(context))


class IndexView_not_used(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_post_list'
    paginate_by = 10
    model = Post
    
    def get_queryset(self):
        """Return the last five published polls."""
        return Post.objects.order_by('-published') #first 5 items order by published desc





# this is a old way to serve post page
#def post_old(request, post_id):
#    try:
#        post = Post.objects.get(pk=post_id)
#    except Post.DoesNotExist:
#        raise Http404
#    context = {'post': post}
#    return render(request, 'blog/post.html', context)


# this is the laziest way to serve page
def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    has_next = True
    has_previous = True
    next_post = 0
    previous_post = 0
    try:
        next_post = post.get_next_by_created().id
    except Post.DoesNotExist:
        has_next = False
    
    try:    
        previous_post = post.get_previous_by_created().id
    except Post.DoesNotExist:
        has_previous = False

    return render(request, 'blog/post.html', {
        'post': post,
        'has_next': has_next,
        'has_previous': has_previous,
        'next': next_post,
        'previous': previous_post,
    })

 

class PostView_not_used(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'
     

def add_comment(request, post_id):
    p = get_object_or_404(Post, pk=post_id)
    try:    #if request.POST['comment'] or visiterName=request.POST['visitor'] does not exist in request, KeyError will be thrown
        #Todo: need to do empty value check here
        c = Comment(body=request.POST['comment'], ip='127.0.0.1', visitorName=request.POST['visitor'], post=p)
    except(KeyError, Post.DoesNotExist):
        return render(request, 'blog/post.html',{
            'post': p,
            'error_message': "Failed to submit comment.",
        })
    else:
        c.save()
        return HttpResponseRedirect(reverse('blog:post', args=(p.id, )));

def category(request, cate_id):
    category = get_object_or_404(Category, id=cate_id)
    posts_by_catetory = get_list_or_404(Post, category_id = cate_id)    
    return render(request, 'blog/category.html', {
        'posts_by_catetory': posts_by_catetory,
        'category': category
    })


def tag(request, t_id):
    tag = get_object_or_404(Tag, id=t_id)
    posts_by_tag = tag.post_set.all();
    paginator = Paginator(posts_by_tag, 5)
    page = request.GET.get('page')
    
    try:
        latest_posts = paginator.page(page)
    except PageNotAnInteger:
        latest_posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        latest_posts = paginator.page(paginator.num_pages)
    
    return render(request, 'blog/tag.html',{
        'tag': tag,
        'latest_posts': latest_posts
    })

  











