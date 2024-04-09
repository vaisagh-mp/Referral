from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from .models import User, Referral
from .serializers import UserSerializer, ReferralSerializer
from rest_framework.permissions import AllowAny

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserDetailsView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    

    def get_object(self):
        return self.request.user

class ReferralsView(generics.ListAPIView):
    serializer_class = ReferralSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Referral.objects.filter(referrer=self.request.user)

