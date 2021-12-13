
from django.contrib import messages
from django.shortcuts import render
from vedio.models import Item,Category,vedioComment
from django.urls import reverse
from django.http.response import HttpResponseRedirect



# Create your views here.

def categorylist(request):
    print("categorylist is called")
    categories=Category.objects.all()
    context={'categories':categories}
    return render(request,'vedio/categorylist.html',context)

def categoryvedio(request,slug):
    print("categoryvedio is called")
    categories=Category.objects.filter(slug=slug).first()
    catvedios=Item.objects.filter(category=categories)
    context={'catvedios':catvedios}
    return render(request,'vedio/catvedio.html',context)

def videodetail(request,slug):
    print("vediodetail is called")
    video=Item.objects.filter(slug=slug).first()
    comments=vedioComment.objects.filter(video=video,parent=None)
    replies=vedioComment.objects.filter(video=video).exclude(parent=None)
    repDict={}
    for reply in replies:
        if reply.parent.srno not in repDict.keys():
            repDict[reply.parent.srno]=[reply]
        else:
            repDict[reply.parent.srno].append(reply)
    context={'videos':video,'comments':comments,'user':request.user,'repDict':repDict}
    print(comments)
    print(repDict)
    return render(request,'vedio/videodetail.html',context)

def comment(request):
    print("fhdjhkid")
    
    videocomment=request.POST.get('commentbox')
    print(videocomment)
    videosno=request.POST.get('videoSno')
    print(videosno)
    video=Item.objects.get(id=videosno)
    parentSno=request.POST.get('parentSno')
    print(parentSno)
    user=request.user

    if parentSno=="":
        comment1=vedioComment(comment=videocomment,user=user,video=video)
        comment1.save()
        messages.success(request,"your comment has been posted successfully")
        return HttpResponseRedirect(reverse('vedio:videodetail',args=(video.slug,)))
    else:
        parent=vedioComment.objects.get(srno=parentSno)
        comment1=vedioComment(comment=videocomment,user=user,video=video,
        parent=parent)
        comment1.save()
        messages.success(request,"you replay has been added")
        return HttpResponseRedirect(reverse('vedio:videodetail',args=(video.slug,)))