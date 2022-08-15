from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import generic

from common.utils import generateOTP
from hotMops.settings import EMAIL_HOST_USER
from userApp.forms import SignInForm, SignUpForm


def index(request):
    return render(request, 'landingpage.html')


class SignUp(generic.View):
    form = SignUpForm
    template_name = "registration/signup.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/home')
        form = self.form()
        return render(
            request,
            self.template_name,
            {"form": form},
        )

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            form.data = form.cleaned_data
            print(form.data)
            obj = form.save(commit=False)
            obj.user = form.data['user']
            obj.save()
            # form.save()
            user = authenticate(username=form.data['email'], password=form.data['password'])
            if user:
                login(request, user)
                messages.success(request, "Successfully Registered and Logged In")
                return redirect('/home')
        else:
            print('Form not valid')
            return redirect("/accounts/sign-up")


def send_otp(request):
    email = request.POST.get("email")
    o = generateOTP()
    htmlgen = f'<p>Your OTP is <strong>{o}</strong></p>'
    status = send_mail('OTP request', o, EMAIL_HOST_USER, [email], fail_silently=False, html_message=htmlgen)
    if status:
        return HttpResponse(o)
    else:
        return HttpResponse("False")


def log_out(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully!')
    return redirect("/")


class SignIn(generic.View):
    form = SignInForm
    template_name = "registration/login.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/home')
        form = self.form()
        return render(
            request,
            self.template_name,
            {"form": form},
        )

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            form.data = form.cleaned_data
            user = authenticate(username=form.data['username'], password=form.data['password'])
            if user:
                login(request, user)
                messages.success(request, "Logged In Successfully!")
                return redirect("/home")
            else:
                messages.success(request, "Invalid Credentials!")
                return redirect("/accounts/sign-in")

