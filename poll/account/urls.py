from django.urls import path 

from .views import (
    login_view, signup_view,
    result_view, logout_view,
    select_position_view, vote_view
)


app_name = "account"
urlpatterns = [
    path("signup/", signup_view, name="signup_view"),
    path("login/", login_view, name="login_view"),
    path("logout/", logout_view, name="logout_view"),
    path("view-poll-result/", result_view, name="result_view"),
    path("vote/", select_position_view, name="select_position_view"),
    path("vote/<str:candidate_id>/", vote_view, name="vote_view"),
    
]
