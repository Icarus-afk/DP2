from django.shortcuts import redirect, render
from .models import Family, Charity, Culture, Business, Venue, Contact_us, Book_event, Food
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
from django.conf import settings


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
    fam = Family.objects.all()
    return render(request, 'family.html', {'f': fam})


def charity(request):
    chari = Charity.objects.all()
    return render(request, 'charity.html', {'c': chari})


def business(request):
    bus = Business.objects.all()
    return render(request, 'business.html', {'b': bus})


def culture(request):
    cul = Culture.objects.all()
    return render(request, 'culture.html', {'cu': cul})


def venue(request):
    ven = Venue.objects.all()
    return render(request, 'venue.html', {'v': ven})

def food(request):
    food_p = Food.objects.all()
    return render(request, 'food.html', {'f': food_p})


@login_required(login_url='login')
def book_event(request):
    fooddrop = Food.objects.all()
    venuedrop = Venue.objects.all()
    if request.method == "POST":
        Name = request.POST['name']
        Mobile = request.POST['mobile']
        Email = request.POST['email']
        People = request.POST['people']
        Date = request.POST['date']
        Event = request.POST['event']
        Address = request.POST['address']
        Foods = request.POST['foods']
        food = Food.objects.get(pk=Foods)
        venue_temp = request.POST['venue']
        venuepk = Venue.objects.get(pk=venue_temp)
        Message = request.POST['message']
        cpct = int(venuepk.capacity)
        input_cpct = int(People)
        
        
        bill = (int(food.pack_price)*input_cpct+int(venuepk.price))
        finalbill = bill + bill*0.5
        if ((Mobile and Email and Address) == ""):
            messages.info(request, 'Warning field required')
            return redirect('/bookevent')
        elif (input_cpct > cpct):
            messages.info(request, "warning! capcity exceeded!")
            return redirect('/bookevent')

        else:
            guest = Book_event(name=Name, mobile=Mobile, email=Email, venue=venuepk, people=People,
                               date=Date, event=Event, food=food, address=Address, message=Message, bill = finalbill)
            guest.user = request.user
            guest.name = request.user
            guest.save()
            messages.info(
                request, "Your Event is booked successfully! Thank you for booking an event with us!")
            return redirect('/')
    return render(request, 'book.html', context={'fd': fooddrop, "vn": venuedrop})


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
                messages.info(request, "Username already exist!")
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exist!")
                return redirect('/register')
            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                user.save()
                messages.info(
                    request, 'Your account has been created successfully! Please login')
                return redirect('/login')
        else:
            messages.info(request, "Password didn't match")
            return redirect('/register')

    else:

        return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid username/ password!')
            return redirect('/login')
    else:
        return render(request, 'login.html')


def change_password(request):
    if request.method == "GET":
        pc = PasswordChangeForm(user=request.user)
        return render(request, 'changepassword.html', {'context': pc})
    elif request.method == "POST":
        aa = PasswordChangeForm(user=request.user,  data=request.POST)
        if aa.is_valid():
            user = aa.save()
            update_session_auth_hash(request, user)
            messages.info(
                request, "Password Changed Successfully! Login again")
            return redirect("/login")


def usercart(request):
    my_cart = Book_event.objects.filter(user=request.user)
    return render(request, 'user_cart.html', {'my_cart': my_cart})


def aboutus(request):
    return render(request, "aboutus.html")


def logout(request):
    auth.logout(request)
    return redirect("/")
