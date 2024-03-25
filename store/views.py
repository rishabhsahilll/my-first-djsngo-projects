from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import UserDta, UserProfile
from django.db.utils import IntegrityError
# from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.decorators import login_required
import cloudinary
from cloudinary.uploader import upload
import os
import environ

# .env file ka path set karein
env = environ.Env()

# Cloudinary configuration
cloudinary.config(
    cloud_name="rishabh-insta",
    # api_key=env('IMG_API_KEY'),
    # api_secret=env('IMG_API_SECRET')
    api_key='188728799314739',
    api_secret='Vuog68Ts8G7f1X-pDnd5bd0n480'
)

# Create your views here.
@csrf_exempt
def index(request):
    try: 
        if request.user.is_authenticated:
            user_profile = UserProfile.objects.get(user=request.user)
            context = {
                'f_name': user_profile.first_name,
                'l_name': user_profile.surname,
                'email': user_profile.email,
                'address_line1': user_profile.address_line1,
                'address_line2': user_profile.address_line2,
                'mobile': user_profile.mobile_number,
                'pcode': user_profile.postcode,
                'state': user_profile.state,
                'area': user_profile.area,
                'region': user_profile.state_region,
                'edu': user_profile.education,
                'cont': user_profile.country, 
                'image': user_profile.image,
            }
            return render(request, 'home.html',context)
    except UserProfile.DoesNotExist:
        return redirect('create')
    return render(request, 'login-signup.html')

@csrf_exempt
def singup(request):
    _messages = ''
    alart = ''
    username = ''
    email = ''

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if len(username) < 4:
            _messages = 'Username must be more than 4!'
            display = 'block'
            display = 'block'
            alart = 'danger'
        elif len(password) < 8:
            _messages = 'Password must be more than 8!'
            display = 'block'
            alart = 'danger'
        elif password != password2:
            _messages = 'Please check confirm password!'
            display = 'block'
            alart = 'danger'
        else:
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                _messages = 'User created successfully!'
                display = 'block'
                alart = 'success'
            except IntegrityError:
                _messages = 'Username already exists!'
                display = 'block'
                alart = 'danger'

    context = {
        'msg': _messages,
        'al_msg': alart,
        'dis': display,
        'username': username,
        'email': email,
    }
    return render(request, 'login-signup.html', context)

@csrf_exempt
def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            print("Okk")
            return redirect('home')
        else:
            context = {
            'msg': "Please check your username and password!",
            'al_msg': "danger",
            'dis': 'block',
        }
            return render(request, 'login-signup.html',context)
            
    return redirect('home')

def userlogout(request):
    logout(request)
    return redirect('login')

@login_required
def create(request):
    if request.method == 'POST':
        user = request.user
        first_name = request.POST.get('fname')
        surname = request.POST.get('lname')
        mobile_number = request.POST.get('mobile')
        address_line1 = request.POST.get('ad1')
        address_line2 = request.POST.get('ad2')
        postcode = request.POST.get('postcode')
        state = request.POST.get('state')
        area = request.POST.get('area')
        email = request.POST.get('email')
        education = request.POST.get('edu')
        country = request.POST.get('cont')
        state_region = request.POST.get('region')
        imagepath = request.FILES.get('imagepath')
        print(imagepath)
        if imagepath is not None:
            result = upload(imagepath, folder=f"{request.user.username}")
            try:
                # Create UserProfile instance
                user_profile = UserProfile.objects.create(
                    user=user,
                    first_name=first_name,
                    surname=surname,
                    mobile_number=mobile_number,
                    address_line1=address_line1,
                    address_line2=address_line2,
                    postcode=postcode,
                    state=state,
                    area=area,
                    email=email,
                    education=education,
                    country=country,
                    state_region=state_region,
                    image=result['secure_url']
                )
                # Update user's first and last name
                user.first_name = first_name
                user.last_name = surname
                user.save()
                user_profile.save()

                return redirect('profile')
            except Exception as e:
                # Handle any errors that might occur during creation
                print(f"Error: {e}")
                # Add appropriate error handling or redirect to an error page
                # For now, let's redirect back to the form page with an error message
                return redirect('profile')
        else:
            try:
                # Create UserProfile instance
                user_profile = UserProfile.objects.create(
                    user=user,
                    first_name=first_name,
                    surname=surname,
                    mobile_number=mobile_number,
                    address_line1=address_line1,
                    address_line2=address_line2,
                    postcode=postcode,
                    state=state,
                    area=area,
                    email=email,
                    education=education,
                    country=country,
                    state_region=state_region
                )
                # Update user's first and last name
                user.first_name = first_name
                user.last_name = surname
                user.save()
                user_profile.save()

                return redirect('profile')
            except Exception as e:
                # Handle any errors that might occur during creation
                print(f"Error: {e}")
                # Add appropriate error handling or redirect to an error page
                # For now, let's redirect back to the form page with an error message
                return redirect('profile')

    # Handle GET request or any other request method
    context = {
        'image': 'static/images/ico_def.png',
        'display': 'none',
        'url': 'profileedit',
        'btntxt': 'Edit Profile'
    }
    return render(request,'profile.html',context)


def profile(request):
    try:
        if request.user.is_authenticated:
            user_profile = UserProfile.objects.get(user=request.user)
            
            # Extract data from the user_profile object
            f_name = user_profile.first_name 
            l_name = user_profile.surname
            email = user_profile.email
            address_line1 = user_profile.address_line1
            address_line2 = user_profile.address_line2
            mobile = user_profile.mobile_number
            postcode = user_profile.postcode
            state = user_profile.state
            area = user_profile.area
            region = user_profile.state_region
            edu = user_profile.education
            cont = user_profile.country
            img = user_profile.image
            # print(img)
            context = {
                'f_name': f_name,
                'l_name': l_name,
                'email': email,
                'address_line1': address_line1,
                'address_line2': address_line2,
                'mobile': mobile,
                'pcode': postcode,
                'state': state,
                'area': area,
                'region': region,
                'edu': edu,
                'cont': cont, 
                'image': img,
                'display': 'block',
                'url': 'profileedit',
                'btntxt': 'Edit Profile',
                'display2': 'none',

                # Add other fields as needed
            }
            return render(request, 'userinfo.html', context)
        else:
            return redirect('login')
    except UserProfile.DoesNotExist:
        return redirect('create')
    
@login_required
def profileedit(request):
    if request.method == 'POST':
        user_profile = UserProfile.objects.get(user=request.user)
        user_profile.first_name = request.POST.get('fname')
        user_profile.surname = request.POST.get('lname')
        user_profile.mobile_number = request.POST.get('mobile')
        user_profile.address_line1 = request.POST.get('ad1')
        user_profile.address_line2 = request.POST.get('ad2')
        user_profile.postcode = request.POST.get('postcode')
        user_profile.state = request.POST.get('state')
        user_profile.area = request.POST.get('area')
        user_profile.email = request.POST.get('email')
        user_profile.education = request.POST.get('edu')
        user_profile.country = request.POST.get('cont')
        user_profile.state_region = request.POST.get('region')
        
        current_user = request.user
        current_user.first_name = request.POST.get('fname')
        current_user.last_name = request.POST.get('lname')
        
        imagepath = request.FILES.get('imagepath')
        if imagepath is not None:
            result = upload(imagepath, folder=f"{request.user.username}")
            user_profile.image = image=result['secure_url']
        
        current_user.save()
        user_profile.save()
        return redirect('profile')
        
    else:
        user_profile = UserProfile.objects.get(user=request.user)
        context = {
            'f_name': user_profile.first_name,
            'l_name': user_profile.surname,
            'email': user_profile.email,
            'address_line1': user_profile.address_line1,
            'address_line2': user_profile.address_line2,
            'mobile': user_profile.mobile_number,
            'pcode': user_profile.postcode,
            'state': user_profile.state,
            'area': user_profile.area,
            'region': user_profile.state_region,
            'edu': user_profile.education,
            'cont': user_profile.country, 
            'image': user_profile.image,
            'display': 'none',
            'url': 'profileedit',
            'btntxt': 'Update Profile'
        }
        return render(request,'userinfo.html', context)
    

def custom_password_reset(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = None
            if user is not None:
                form.cleaned_data['email'] = user.email
                return form.save(request=request)
    else:
        form = PasswordResetForm()
    return render(request, 'password_reset.html', {'form': form})

def chat(request):
    # Query the UserProfile object associated with the current user
    user_profile = UserProfile.objects.get(user=request.user)

    # Get the URL of the image associated with the user profile
    custom_image_url = user_profile.image.url if user_profile.image else None

    # Query all users
    all_users = User.objects.all()

    # Get admin user
    admin_user = User.objects.filter(is_staff=True).first()
    admin_image_url = None
    if admin_user:
        admin_profile = UserProfile.objects.filter(user=admin_user).first()
        admin_image_url = admin_profile.image.url if admin_profile and admin_profile.image else None

    # Iterate through each user and extract required fields
    user_data = []
    for user in all_users:
        # Check if the user is admin
        is_admin = user.is_staff

        # Get the image URL based on user type
        if is_admin:
            image_url = admin_image_url
        else:
            image_url = custom_image_url

        user_info = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'image_url': image_url,  # Include the image URL in user data
            'is_admin': is_admin,  # Include whether the user is admin or not
        }
        user_data.append(user_info)


    return render(request, 'chat.html',{'user_data': user_data})
