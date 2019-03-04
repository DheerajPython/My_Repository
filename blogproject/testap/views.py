from django.shortcuts import render,get_object_or_404
from testap.models import Post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.core.mail import send_mail
from testap.forms import EmailSendForm
from testap.models import Comment
# Create your views here.
def Post_List_View(request):
    post_list=Post.objects.all()
    paginator=Paginator(post_list,2)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'testap/post_list.html',{'post_list':post_list})
def Post_Detail_View(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,status='publish',publish__year=year,publish__month=month,publish__day=day)
    return render(request,'testap/post_detail.html',{'post':post})
def Email_Send_View(request,id):
    post=get_object_or_404(Post,id=id,status='publish')
    sent=False
    if request.method=='POST':
        form=EmailSendForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            post_url=request.build_absolute_uri(post.get_absolute_url())
            subject='{}  ({}) recommends you to read  {} '.format(cd['name'],cd['email'],post.title)
            message='Read Post At : \n{}\n\n {}\'s comment:\n{}'.format(post_url,cd['name'],cd['comments'])
            send_mail(subject,message,'Blog',[cd['to']])
            sent=True
    else:
        form=EmailSendForm()
    return render(request,'testap/sharebymail.html',{'form':form,'post':post,'sent':sent})
