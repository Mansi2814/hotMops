from django.urls import path, include
from .views import SignIn, SignUp, index, log_out, send_otp

urlpatterns = [
    path('', index, name="landingpage"),
    path('accounts/sign-up/', SignUp.as_view(), name="signup"),
    path('accounts/sign-in/', SignIn.as_view(), name="signup"),
    path('accounts/logout/', log_out, name="logout"),
    path('accounts/send-otp/', send_otp, name="send_otp"),
    path('accounts/', include('django.contrib.auth.urls')),
]