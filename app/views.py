from django.shortcuts import render,redirect
from app.models import productModels,registerModels,cart_itemModel,cartModel

# login model
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
# Create your views here.
# email
from django.core.mail import send_mail
from django.shortcuts import render

# decorater
# from django.contrib.auth.decorators import login_required
# @login_required(login_url='/login_form')
def reg_form(request):
    if request.method == "POST":
        F_name = request.POST['first_name']
        L_name = request.POST['last_name']
        U_name = request.POST['user_name']
        Email = request.POST['email']
        T_number = request.POST['tel_number']
        Address = request.POST['address']
        Gender = request.POST['gender']
        distic = request.POST['distic']
        Password = request.POST['password']
        coform_password = request.POST['conf_password']
           
        #  nummel kodutha username ithil undo ann chack chayyunnu
        if User.objects.filter(username = U_name ):
            message = 'sory the custemer already exist .....'
            print('user Exist')
            return render(request,'register.html')
        else:
            if Password == coform_password :
                if User.objects.filter(username = U_name):
                    return render(request,'register.html')
        
                else:
                    
                    
                    user = User.objects.create_superuser(
                        first_name = F_name,
                        last_name = L_name,
                        username = U_name,
                        email = Email,
                        password = Password 
                        )
                    user.save()
                    Newuser = registerModels(
                        # models ile kodutha 'c_user' anna varible lek ,mukalil kodutha 'User' models nte objectine assing chayyunnu
                        c_user = user, 
                        Tel_number = T_number,
                        Address = Address,
                        gender = Gender,
                        destic = distic )
                    Newuser.save()
                    
                    # SEND EMAIL
                    subject = 'Hello, Django Email!'
                    message = 'this is text email sent from django'
                    from_email = 'rashi3225@gmail.com'
                    recipient_list = [user.email,]
                    
                    send_mail(subject,message,from_email,recipient_list)
                    
                    # login authentication
                    userdata = authenticate(username = U_name,
                                            password = Password )
                    if userdata is not None:
                       login(request, userdata)
                       print('success')
                       return redirect('index_page')
                    else:
                        return redirect('reg_form')
                   
                   
                    
                    
                    
                    
        
                    
                    # return redirect('login_form')
            else:
                print('password note matching')
                return redirect('reg_form')
    else:
        print('please check your method is "POST" ')
        return render(request,'register.html')                
                    
            
            
            
        
        
        


# login

def login_form(request):
    if request.method == 'POST':
        
        usename = request.POST['username']
        Password = request.POST['password']
        
        user = authenticate(request, username=usename,password=Password)
        if user is not None:
            login(request, user)
            return redirect ('index_page')
        else:
            return render(request,'login.html')
    else:
        return render (request,'login.html')
# logout
def userlogout(request):
    logout(request)
    return redirect ('login_form')

# signup

# product_form
def prod_form(request):
    if request.method == 'POST':
        prod_id = request.POST['Prouct_id']
        prod_name = request.POST['Product_name']
        prod_price = request.POST['Product_price']
        prod_desc = request.POST['Product_desc']
        prod_image = request.FILES.get('Product_image')
        
        newProdect = productModels (Prod_Id = prod_id,prod_Name = prod_name,Prod_Price = prod_price,Prod_Desc = prod_desc,Prod_image = prod_image)
        newProdect.save()
        print('success')
        return render (request,'product_form.html')
    else:
        return render (request,'product_form.html')
# voew product
def view_product(request):
    product = productModels.objects.all()
    return render(request,'view_product.html',{'product':product})
# home

def index(request):
    product = productModels.objects.all()
    return render(request,'index.html',{'product':product})

def card(request):
    product = productModels.objects.all()
    return render (request,'product.html',{'product':product})

# cart
def add_to_cart(request,i):
    current_user = request.user
    item = productModels.objects.get(id=i)
    qty = 1
    price = item.Prod_Price
    
    try:
        user_cart = cartModel.objects.get(user = current_user)
        new_cart_item = cart_itemModel(item = item,quantity = qty,price = price)
        new_cart_item.save()
        user_cart.item.add(new_cart_item)
        user_cart.save()
    except:
        user_cart = cartModel(user = current_user)
        user_cart.save()
        new_cart_item = cart_itemModel(item = item,quantity = qty,price = price)
        new_cart_item.save()
        user_cart.item.add(new_cart_item)
        user_cart.save()
        
    print('item added')
    return redirect('cart')

# view addToCart items

def cart_page(request):
    current_user = request.user
    cart = cartModel.objects.get(user = current_user)
    cart_items = cart.item.all()
    # cart_items.delete()
    
    return render (request,'cart.html',{'cart_item':cart_items})

# delete cart item
def delete_cart(request,item_id):
    current_user = request.user  
    user_cart = cartModel.objects.get(user = current_user)
    items = cart_itemModel.objects.get(id = item_id )
    user_cart.item.remove(items)
    user_cart.save()
    
    return redirect('cart')
    
# delete all cart item
def delete_all_items(request):
    current_user = request.user
    cart = cartModel.objects.get(user = current_user)
    cart_items = cart.item.clear()
    
    return redirect('cart')


    