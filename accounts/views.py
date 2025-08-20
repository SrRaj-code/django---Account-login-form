from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib import messages

def create_account_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if UserProfile.objects.filter(email=email).exists():
            messages.error(request, 'This email address is already in use. Please use a different one.')
            return render(request, 'index.html')

        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        
        hobbies_list = request.POST.getlist('hobbies')
        hobbies = ', '.join(hobbies_list)
        
        source_of_income = request.POST.get('source')
        income = request.POST.get('income')
        age = request.POST.get('age')
        bio = request.POST.get('bio')
        profile_picture = request.FILES.get('profile')

        new_user = UserProfile(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password, 
            gender=gender,
            hobbies=hobbies,
            source_of_income=source_of_income,
            income=income,
            age=age,
            bio=bio,
            profile_picture=profile_picture
        )
        
        new_user.save()
        messages.success(request, 'Account created successfully!')
        return redirect('create_account') 

    return render(request, 'index.html')