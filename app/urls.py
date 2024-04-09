from django.urls import path
from .views import RegisterUserView, UserDetailsView, ReferralsView

urlpatterns = [
    path('api/register/', RegisterUserView.as_view(), name='register'),
    path('api/user/details/', UserDetailsView.as_view(), name='user-details'),
    path('api/user/referrals/', ReferralsView.as_view(), name='user-referrals'),
]
