from django.shortcuts import render

from .models import Family, Charity, Culture, Business, Venue, Contact_us, Book_event
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from


def home(request):
    if request.method = "POST":
        Name = request.POST["name"]
        Mobile = request.POST["mobile"]
        Email = request.POST["email"]
        Message = request.POST["message"]
        
        enquiry = Contact_us(name = Name, mobile = Mobile, email = Email, message = Message)
        enquiry.save()
        messages.info(request , "Your Query has been sent successfully! ")
        return redirect("/")
    return render(request, "home.html")

def family(request):
    fam = Family.object.all()
    return render(request, 'family.html', {f:fam})

def charity(request):
    chari = Charity.object.all()
    return render(request, 'charity.html', {c:chari})

def business(request):
    bus = Business.object.all()
    return render(request, 'business.html', {b:bus})

def culture(request):
    cul = Culture.object.all()
    return render(request, 'culture.html', {cu:cul})

def venue(request):
    ven = Venue.object.all()
    return render(request, 'venue.html', {v:ven})

@login_required(login_url = 'login')
def book_event(request):
    if request.method = "POST":
        Name = request.POST['name']
        Mobile = request.POST['mobile']
        Email = request.POST['email']
        People = request.POST['people']
        Date = request.POST['date']
        Event = request.POST['event']
        Address = request.POST['address']
        Venue = request.POST['venue']
        Message = request.POST['message']
        if ((Mobile and Email and Address and Name)=="":
            message.info(request, "Warning! Field missing!"))
            return redirect("/bookevent")
        else:
            book = (name = Name, mobile = Mobile, email = Email, people = People, date = Date, event = Event, food = Food, address = Address, message = Message)
            book.user = request.user
            book.name = request.user
            book.save()
            message.info(request, "Thank you for your booking, The event has been booked successfully!")
            return redirect("/")
    
    return render(request, "book.html")


def about_us(request):
    return render(request, "aboutus.html")

def register(request):
    if request.method = "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                message.info(request, "Username already exists")
                return redirect("/register")
            elif:
                User.objects.filter(email = email).exists():
                    message.info(request, "Email already used")
                    return redirect('/register')
            else:
                user = User.objects.create_user(first_name = first_name, last_name = last_name, username = username, email = email, password = password)
                user.save()
                message.info(request, "Your account has been created successfully! Please log in")
        else:
            message.info(request, "Password did not match")
            return redirect("/register")
    else:
        return render(request, "register.html")
    
def user_date(request):
    data = User.objects.filter(User = request.user)
    return render(request, "user.html", {u : data})

#, user data, login, password_change, cart, logout
