from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from blog1.models import POST
from home.models import Contact

# Create your views here.

def homepage(request):
    return render(request,'home/index.html')

def signup(request):
    if request.method=='POST':
         
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        username=request.POST['username']
        confirmpassword=request.POST['confirm password']
        if name=="":
            messages.info(request,"Name should not be empty")
            return redirect("/register")
        elif email=="":
            messages.info(request, "email should not be empty")
            return redirect("/register")
        elif password=="":
            messages.info(request, "password should not be empty")
            return redirect("/register")
        elif username=="":
            messages.info(request, "username should not be empty")
            return redirect("/register")
        elif confirmpassword=="":
            messages.info(request, "confirmpassword should not be empty")
            return redirect("/register")
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request, "username not available")
                return redirect("/register")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "email not available")
                return redirect("/register")
            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=name)
                user.save()
                messages.info(request,"Registered Successfully")

        
                auth.login(request,user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('/')

    else:
        return render(request,'home/register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.info(request,"Login Sucessfully")
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')

        else:
            messages.error(request,"Check Username or Password")
            return redirect('/login')
    else:
            return render(request,'home/login.html')
    
def logout(request):
    auth.logout(request)
    return redirect("/")

def contactus(request):
    if request.method=='POST':
        name=request.POST['name']
        username=request.POST['username']
        msg=request.POST['message']
        email=request.POST['email']
        contact=request.POST['contact']
        c=Contact(name=name,username=username,contactno=contact,email=email,msg=msg)
        c.save()
        messages.success(request,"Thanks for contacting. We will get back soon")
        return redirect('/contact')
    else:
        return render(request,'home/contact.html')   



def search(request):
    query=request.GET['query']
    
    if(len(query)>60):
        posts=POST.objects.none()
    else:
        posttitles=POST.objects.filter(title__icontains=query)
        postcontents=POST.objects.filter(desc__icontains=query)
        posts=posttitles.union(postcontents)
    if posts.count()==0:
        messages.warning(request,"No search result found")
    context={'posts':posts, 'query':query}

    return render(request,"home/search.html",context)