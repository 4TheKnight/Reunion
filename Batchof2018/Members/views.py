from django.shortcuts import render,redirect
from .forms import UserCreationForm , ProfileForm,Customusercreation, post_form
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.http import HttpResponse
from .models import Profile,post,comments
from django.shortcuts import get_object_or_404

@login_required
def show_post(request):
    data = post.objects.all()
    return render(request,'Home/Home.html',{'data':data})


def register(request):
    if request.method =="POST":
        form = Customusercreation(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('register')
    else:
        form= Customusercreation()
    return render(request,'authentication/register.html',{'form':form})

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method =="POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return HttpResponse('Bio Updated')
    else:
        form = ProfileForm(instance=profile)
    return render(request,'authentication/profile.html',{'form':form})

@login_required
def make_post(request):
    if request.method == "POST":
        form = post_form(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            profile = get_object_or_404(Profile,user=request.user)
            post.author = profile
            post.save()
            return redirect('post')
    else:
        form = post_form()
    return render(request,'post/createpost.html',{'form':form})

@login_required
def likepost(request,post_id):
    posts = get_object_or_404(post,id=post_id)
    profile = get_object_or_404(Profile,user = request.user)

    if profile in posts.likes.all():
        posts.likes.remove(profile)
        messages = "Removed Like"
    else:
        posts.likes.add(profile)
        messages = "Liked"

    posts.save()
    response_html = f"""
    <script>
        alert("{messages}");
        window.location.href = '/showpost';  <!-- Redirect to home page -->
    </script>
    """
    return HttpResponse(response_html)

@login_required
def makecomment(request,post_id):
    if request.method == "POST":
        posts = get_object_or_404(post,id=post_id)
        profile = request.user
        user_comment = request.POST.get('comment')
        new_comment = comments.objects.create(post = posts, author=profile,comment=user_comment)

        new_comment.save()
    response_html = f"""
    <script>
        alert("comment added");
        window.location.href = '/showpost';  <!-- Redirect to home page -->
    </script>
    """
    return HttpResponse(response_html)
@login_required
def showcomments(request, post_id):
    comment  = comments.objects.filter(post=post_id)
    return render(request,'Home/Comments.html',{'comment':comment})

@login_required
def liked_by(request, post_id):
    liked_post = get_object_or_404(post, id=post_id)
    liked_by = liked_post.likes.all()
    return render(request,'Home/showliked.html',{'liked_by':liked_by})

@login_required
def view_profile(request,profile_user):
    user = get_object_or_404(User,username=profile_user)
    user_profile = get_object_or_404(Profile,user=user)
    return render(request,'Home/profile.html',{'user_profile':user_profile})

@login_required
def delete_user(request):
    if request.method == 'POST':  # Make sure the request is POST
        user = request.user
        user.delete()  # Delete the user
        return HttpResponse('User Deleted')  # Redirect to home after deletion
    else:
        print(6)
        return HttpResponse('Only POST method is allowed to delete a user.')

@login_required
def delete_post(request,post_id):
    postdata = get_object_or_404(post,id=post_id)

    if(postdata.author.user==request.user):
        postdata.delete()
        return redirect('post')
    
def home(request):
    return redirect('login')