from django.shortcuts import redirect, render
from .models import Family, Charity, Culture, Business, Venue, Contact_us, Book_event
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User, auth


def home(request):
    if request.method == "POST":
        Name = request.POST["name"]
        Mobile = request.POST["mobile"]
        Email = request.POST["email"]
        Message = request.POST["message"]

        enquiry = Contact_us(name=Name, mobile=Mobile,
                             email=Email, message=Message)
        enquiry.save()
        messages.info(request, "Your Query has been sent successfully! ")
        return redirect("/")
    return render(request, "home.html")


def family(request):
    fam = Family.object.all()
    return render(request, 'family.html', {'f': fam})


def charity(request):
    chari = Charity.object.all()
    return render(request, 'charity.html', {'c': chari})


def business(request):
    bus = Business.object.all()
    return render(request, 'business.html', {'b': bus})


def culture(request):
    cul = Culture.object.all()
    return render(request, 'culture.html', {'cu': cul})


def venue(request):
    ven = Venue.object.all()
    return render(request, 'venue.html', {'v': ven})


@login_required(login_url='login')
def book_event(request):
    if request.method == "POST":
        Name = request.POST['name']
        Mobile = request.POST['mobile']
        Email = request.POST['email']
        People = request.POST['people']
        Date = request.POST['date']
        Event = request.POST['event']
        Address = request.POST['address']
        Food = request.POST['food']
        Venue = request.POST['venue']
        Message = request.POST['message']
        if (Mobile and Email and Address and Name) == "":
            messages.info(request, "Warning! Field missing!")
            return redirect("/bookevent")
        else:
            book = Book_event(name=Name, mobile=Mobile, email=Email, people=People, date=Date, event=Event, food=Food, address=Address, venue=Venue, message = Message)
            book.user = request.user
            book.name = request.user
            book.save()
            messages.info(
                request, "Thank you for your booking, The event has been booked successfully!")
            return redirect("/")

    return render(request, "book.html")


def about_us(request):
    return render(request, "aboutus.html")


def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect("/register")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already used")
                return redirect('/register')
            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                user.save()
                messages.info(
                    request, "Your account has been created successfully! Please log in")
        else:
            messages.info(request, "Password did not match")
            return redirect("/register")
    else:
        return render(request, "register.html")


def user_data(request):
    data = User.objects.filter(User=request.user)
    return render(request, "user.html", {'u': data})

# ,, login, password_change, cart, logout
def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect("/register")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
            else:
                user = User.objects.create_user(first_name = first_name, last_name = last_name, username = username, email = email, password=password1)
                user.save()
                messages.info(request, "Your account has been created succeessfully! Please login")
                return redirect("/redirect")
        else:
            messages.info(request, "password didn't match")
            return redirect("/register")  
    else:
        return render("/register")
    
    
def login(request):
    if  request.method == "GET":
        pc = PasswordChangeForm(user = request.user)
        return render(request, 'changepassword.html', {'context':pc})
    elif request.method == "POST":
        aa=PasswordChangeForm(user=request.user)
        if aa.is_valid():
            user = aa.save()
            update_session_auth_hash(request, user)
            messages.info(request, "Password changed successfully! Please Login")
            return redirect('/login')
        
        
def change_password(request):
    if request.method == "GET":
        pc = PasswordChangeForm(user = request.user)
        return render(request, 'changepassword.html', {'context': pc})
    elif request.method == "POST":
        aa = PasswordChangeForm(user = request.user,  data = request.POST)
        if aa.is_valid():
            user = aa.save()
            update_session_auth_hash(request, user)
            messages.info(request, "Password Changed Successfully! Login again")
            return redirect("/login")

        
def usercart(request):
    my_cart = Book_event.objects.filter(user = request.user)
    return render(request, "user_cart.html", {'my_cart':my_cart})

def aboutus(request):
    return render(request, "aboutus.html")

def logout(request):
    auth.logout(request)
    return redirect("/")