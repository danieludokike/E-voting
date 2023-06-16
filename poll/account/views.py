# NAMECHEAP ACCOUNT LOGIN
# USERNAME: udokiked
# PASSWORD: Command22__
# EMAIL: udokiked@gmail.com

# domain: premimumnestle.com


# INMOTION HOSTING LOGIN
# USERNAME: KennethOko
# PASSWORD: bRc32g3ppKENNETHoKO
# EMAIL: kennethokonkow67@gmail.com




from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

from pollapp.models import UserProfile, generate_token, Candidate

from .forms import PositionSelectForm

import re

# --------------- TEMPLATE PATHS------------------#
signup_template = "account/signup.html"
login_template = "account/login.html"
select_result_position_templaet = "pollapp/select_result_position.html"
result_template = "pollapp/result.html"

select_vote_position_template = "account/select_voting_position.html"
vote_template = "account/vote.html"
registration_successful_template = "account/registration_successful.html"
# --------------- END TEMPLATE PATHS------------------#


def is_username_valid(username):
    """CHECKS IF THE GIVEN USERNAME IS VALID"""
    if re.match("^[a-zA-Z0-9_.-]+$", username) is not None:
        return True
    return False


def is_username_taken(username):
    """CHECKS IF THE GIVEN USERNAME IS EXISTS IN THE DATABASE"""
    if User.objects.filter(username=username).exists():
        return True
    return False


def is_email_taken(email):
    """CHECKS IF THE EMAIL ADDRESS IS TAKEN BY ANOTHER USER"""
    if User.objects.filter(email=email).exists():
        return True
    return False


def signup_view(request):

    if request.method == "POST":
        first_name = request.POST.get("first_name", None)
        last_name = request.POST.get("last_name", None)
        username = request.POST.get("username", None)
        email = request.POST.get("email", None)
        validation_method = request.POST.get("validation_method", None)
        id_number = request.POST.get("id_number", None)
        
        # # cheking if username is valid
        # if is_username_valid(username):
        #     messages.error(request, f"'{username}' is invalid. Only English letters and numbers are allowed")
        
        # checking if username is taken
        if is_username_taken(username):
            messages.error(request, f"The username '{username}' is  already taken by another user*")
            return redirect("account:signup_view")
        
        # checking if the email is taken
        if is_email_taken(email):
            messages.error(request, f"The email '{email}' is taken by another user")
            
        # saving user details
        user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        user.set_password(generate_token())
        user.save()
        
        # creating user profile
        user_profile = UserProfile.objects.create(
            user=user,
            validation_method=validation_method,
            validation_number=id_number,
            validated=False
            
        )
        user_profile.save()
        
        # sending success message
        success_msg = "We have received your credentials, we will validate it and send feedback to your email on our file. This will will take 24-72 hours. Do check your email and spam folders as well."
        try:
            send_mail(
            f"Account Registration",
            success_msg,
            settings.EMAIL_HOST_USER,
            [email,]
            )
            print("Successful")
        except:
            print("Error")
        return render(request, registration_successful_template, context={"success_msg": success_msg})
        
    return render(request, signup_template, context=None)


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            user_inst = User.objects.get(username=username)
            if not UserProfile.objects.filter(user=user_inst).exists() or  UserProfile.objects.get(user=user_inst).validated == False:
                messages.error(request, "Your accound has not been validated. Please check back later!")
                return redirect("account:login_view")
            else:
                login(request, user)
                messages.success(request, f"Logged in successfully as {username}. You can now cast your vote")
                return redirect("account:select_position_view")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("account:login_view")
        
    return render(request, login_template, context=None)


def result_view(request):
    if request.method == "POST":
        selected_postion = request.POST.get("position", None)
        candidates_in_positions = Candidate.objects.filter(position=selected_postion).order_by("-vote_count")
        
        if len(list(candidates_in_positions)) < 1:
            messages.error(request, f"There is no candidate(s) in '{selected_postion}' category")
            return redirect("account:result_view", permanent=True)
        
        context = {"candidates": candidates_in_positions, "category": selected_postion}
        return render(request, result_template, context=context)
    
    form = PositionSelectForm(request.POST)
    context = {"form": form}
    return render(request, select_result_position_templaet, context=context)


@login_required(login_url="account:login_view")
def select_position_view(request):
    if request.method == "POST":
        selected_postion = request.POST.get("position", None)
        candidates_in_positions = Candidate.objects.filter(position=selected_postion)
        
        if len(list(candidates_in_positions)) < 1:
            messages.error(request, f"There is no candidate(s) in '{selected_postion}' category")
            return redirect("account:select_position_view", permanent=True)
        
        context = {"candidates": candidates_in_positions, "category": selected_postion}
        return render(request, vote_template, context=context)
    
    form = PositionSelectForm(request.POST)
    context = {"form": form}
    return render(request, select_vote_position_template, context=context)


@login_required(login_url="account:login_view")
def vote_view(request, candidate_id):
    if request.method == "POST":
        candidate = Candidate.objects.get(id=candidate_id)
        candidate.vote_count += 1
        candidate.save()
        messages.success(request, f"You have successfully voted for {candidate.candidate_name} as {candidate.position}")
        return redirect("account:select_position_view", permanent=True)
    return redirect("account:select_position_view", permanent=True)


def logout_view(request):
    logout(request)
    return redirect("account:login_view", permanent=True)