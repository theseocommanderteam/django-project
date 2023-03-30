from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from . models import BlogPost
from .forms import CommentForm


# Create your views here.

def Home(request):
    queryset = BlogPost.objects.filter(status = 'published').order_by('-created')
    per_page =3
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    templates_name='home.html'
    contex = {'posts':posts}
    return render(request, templates_name,contex )


def About(request):
    templates_name='about.html'
    contex = {}
    return render(request, templates_name, contex )

# def single_post(request, slug):
#     post = get_object_or_404(BlogPost, slug=slug)
#     templates_name='single.html'
#     contex = {'posts': post}
#     return render(request, templates_name, contex )

def single_post(request, slug):
    template_name = 'single.html'
    # contex = {'posts': post}
    post = get_object_or_404(BlogPost, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'posts': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
