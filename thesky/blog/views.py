from django.shortcuts import render,get_object_or_404
from .models import POST,comment,Project
from.forms import Newcomment


def home(request):
    context={
        'title':'الصفحة الرئيسية',

    'posts': POST.objects.all()
    }
    return render(request,'blog/index.html',context)
def about (request):
    return render(request,'blog/about.html',{'title':'من نحن'})
def post_detail(request,post_id):
  
    post=get_object_or_404(POST,id=post_id)

    comments=post.comments.filter(active=True)
    if request.method=="POST":
        comment_form=Newcomment(data=request.POST)
        #to check befor  save data from comment  form
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            comment_form=Newcomment()
    else:
        comment_form = Newcomment()

    context={
        'title':post,
        'post': post,
        'comments':comments,
        'comment_form':comment_form,

    }


    return render(request,'blog/detail.html',context)
def project_index(request):

    projects = Project.objects.all()

    context = {

        'projects': projects

    }

    return render(request, 'blog/project_index.html', context)
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    context={
         'title':'project',
        'project': project,


       }

    return render(request, 'blog/project_detail.html', context)