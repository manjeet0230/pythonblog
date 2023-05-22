from django.shortcuts import render,get_object_or_404,redirect
from . models import Post



def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_create(request):
 if request.method == 'POST':
    title = request.POST['title']
    content = request.POST['content']
    post =Post.objects.create(title=title, content=content)
    return redirect('post_detail', pk=post.pk)
 return render(request, 'blog/post_create.html')


# def post_edit(request, pk):
#     post = get_object_or_404(post, pk=pk)
#     if request.method == 'POST':
#         post.title = request.POST['title']
#         post.content = request.POST['content']
#         post.save()
#         return redirect('post_detail', pk=post.pk)
#     return render(request, 'blog/post_edit.html', {'post': post})


# def post_delete(request, pk):
#  post = get_object_or_404(post, pk=pk)
#  if request.method == 'POST':
#     post.delete()
#     return redirect('post_list')
#  return render(request, 'blog/post_delete.html', {'post': post})


# rough
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('post_detail', pk=post.pk)
    return render(request, 'blog/post_edit.html', {'post': post})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_delete.html', {'post': post})