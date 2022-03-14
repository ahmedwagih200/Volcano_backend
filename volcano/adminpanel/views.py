from unicodedata import category
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from products.models import *
from products.forms import *
from django.contrib.auth import login, authenticate, logout


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
    prods=Product.objects.all()
    form1=prod_form()
    if req.method=='GET':
               
        return render(req , 'prod.html' , {'prods': prods , 'form1':form1})

    elif req.method=='POST' and 'upname' in req.POST:
        print(req.POST)
        cate=Category.objects.get(id=req.POST['category'])
        Product.objects.filter(id= req.POST['pid']).update(name= req.POST['upname'] , price= req.POST['price'] , category =  cate )  
        
        return render(req , 'prod.html' , {'prods': prods , 'form1':form1})
   
    elif req.method=='POST' and 'abtn' in req.POST:

        form=prod_form(req.POST , req.FILES)
        if form.is_valid():
            form.save()
        
        return render(req , 'prod.html' , {'prods': prods , 'form1':form1})



def del_prod(req , id):

    Product.objects.filter(id=id).delete()

    return HttpResponseRedirect('/admin-prod')


# def upd_prod(req , id):

#     Product.objects.get(id=id)

#     return HttpResponseRedirect('/admin-prod')


def admin_order(req):
    orders=Order.objects.all()
    form= order_form()

    if req.method == 'GET':
        return  render(req , 'order.html' , {'form':form , 'orders':orders} )

    else:
        s=Status.objects.get(id = req.POST['state'])
        Order.objects.filter(id=req.POST['oid']).update(state=s)
        return  render(req , 'order.html' , {'form':form , 'orders':orders} )



def admin_user(req):
    users=User.objects.all()
    form=user_form()
    if req.method=='GET':
        return render(req , 'user.html' ,{'users':users , 'form':form})

    else:
        form1=user_form(req.POST)
        if form1.is_valid():
            form1.save()

        return render(req , 'user.html' ,{'users':users , 'form':form})
    
    

def del_usr(req , id):

    User.objects.get(id=id).delete()
    return HttpResponseRedirect('/admin-user')




def show_items(req , id):
    order=Order.objects.get(id =id)
    ord= order.order_item_set.all()
    return render(req , 'items.html' , {'ord':ord})




def del_cate(req , id):
    Category.objects.filter(id=id).delete()

    return HttpResponseRedirect('/admin-cate')


def login_view(req):

    if req.method == 'GET':
        return render(req , 'login.html')

    else:
        usr=User.objects.filter(email=req.POST['email'],password=req.POST['pwd'] , is_superuser=True )
        #print(usr)
        if len(usr)<1 :
            msg='invalid login data...'
            return render(req, "login.html" ,{'msg':msg})

        else:
            #login(req, usr.first())
            return HttpResponseRedirect('/adminpanel')


def logout_view(req):
    return HttpResponseRedirect('/')
       
