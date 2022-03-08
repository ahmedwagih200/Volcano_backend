from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from products.models import *



def home(req):
    return render(req , 'home.html')


def admin_cate(req):
    if req.method=='GET':

        cates=Category.objects.all()

        return render(req , 'cate.html' , {'cates': cates})

    elif req.method=='POST' and 'cname' in req.POST :
        print(req.POST , req.FILES)
        Category.objects.create(image=req.FILES['cimg'] ,name= req.POST['cname'])

        cates=Category.objects.all()

        return render(req , 'cate.html' , {'cates': cates})
    
    elif req.method=='POST' and 'upname' in req.POST :

        Category.objects.filter(id= req.POST['cid']).update(name= req.POST['upname'])  

        cates=Category.objects.all()

        return render(req , 'cate.html' , {'cates': cates})
    


    

def admin_prod(req):
    pass


def admin_order(req):
    pass


def admin_user(req):
    pass



def del_cate(req , id):
    Category.objects.filter(id=id).delete()

    return HttpResponseRedirect('/admin-cate')