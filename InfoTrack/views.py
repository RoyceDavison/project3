from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from InfoTrack.forms import RegistrationForm,EditProfileForm, PostForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.utils import timezone
# Create your views here.
from .models import User, Comment, Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.time = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    
    return render(request, 'post_detail.html', {'post': post})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.time = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)       
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})



def homepage(request):
    return render(request,"homepage.html")

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/InfoTrack")
    else:
        form = RegistrationForm()
        args = {"form":form}
        return render(request, 'accounts/reg_form.html',args)

@login_required
##否定匿名账户进入／account／profile
def view_profile(request):
    args = {"user": request.user}
    return render(request, 'accounts/profile.html', args)

@login_required
def edit_profile(request):
    if request.method =="POST":
        ###pass user object by instance= request.user
        #change from userchangeform to EditProfileForm
        form = EditProfileForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('/account/profile')
        
    else:
        form = EditProfileForm(instance = request.user)
        args = {"form":form}
        return render(request,"accounts/edit_profile.html",args)

@login_required
def change_password(request):
    if request.method =="POST":
        form = PasswordChangeForm(data = request.POST, user = request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')
        else:
            return redirect('/account/change-password')
    
    else:
        form = PasswordChangeForm(user = request.user)
        args = {"form":form}
        return render(request,"accounts/change_password.html",args)

@login_required
def clubinfo(request):
    try:
        post = Post.objects.order_by("time")[0]
    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    post_title = post.title
    post_time = post.time
    post_context = post.context
    return render(
        request,
        'clubinfo.html',
        context={'post_title':post_title,
                 'post_time':post_time,
                 'post_context':post_context,
                 #'user':user,
                }
        )
@login_required
def freeride(request):
    # Render the HTML template index.html with the data in the context variable
    try:
        post = Post.objects.order_by("time")[0]
    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    post_title = post.title
    post_time = post.time
    post_context = post.context
    return render(
        request,
        'freeride.html',
        context={'post_title':post_title,
                 'post_time':post_time,
                 'post_context':post_context,
                 #'user':user,
                }
        )

@login_required
def courseinfo(request):
    # Render the HTML template index.html with the data in the context variable
    try:
        post = Post.objects.order_by("time")[0]
    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    post_title = post.title
    post_time = post.time
    post_context = post.context
    return render(
        request,
        'courseinfo.html',
        context={'post_title':post_title,
                 'post_time':post_time,
                 'post_context':post_context,
                 #'user':user,
                }
        )
@login_required        
def freeride(request):
    # Render the HTML template index.html with the data in the context variable
    try:
        post = Post.objects.order_by("time")[0]
    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    post_title = post.title
    post_time = post.time
    post_context = post.context
    return render(
        request,
        'freeride.html',
        context={'post_title':post_title,
                 'post_time':post_time,
                 'post_context':post_context,
                 #'user':user,
                }
        )
@login_required        
def privatetutor(request):
    # Render the HTML template index.html with the data in the context variable
    try:
        post = Post.objects.order_by("time")[0]
    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    post_title = post.title
    post_time = post.time
    post_context = post.context
    return render(
        request,
        'privatetutor.html',
        context={'post_title':post_title,
                 'post_time':post_time,
                 'post_context':post_context,
                 #'user':user,
                }
        )
        
@login_required
def rentinfo(request):
    # Render the HTML template index.html with the data in the context variable
    try:
        post = Post.objects.order_by("time")[0]
    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    post_title = post.title
    post_time = post.time
    post_context = post.context
    return render(
        request,
        'rentinfo.html',
        context={'post_title':post_title,
                 'post_time':post_time,
                 'post_context':post_context,
                 #'user':user,
                }
        )