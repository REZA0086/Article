from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import login
import requests
from account.forms import *
import random

from site_settings.models import SiteSettings, SocialMedia


# def generate_random_number():
#     random_number = random.randint(100000, 999999)
#     random_number_str = str(random_number).zfill(6)
#     return random_number_str


class LoginView(View):
    template_name = 'page/account/login.html'

    def get(self, request):
        login_form = LoginForm()
        site_setting = SiteSettings.objects.all().first()
        social_media = SocialMedia.objects.all()
        context = {
            'form': login_form,
            'site_settings': site_setting,
            'social_media': social_media
        }

        return render(request, self.template_name, context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        user_phone = login_form.data['user_phone']
        # code = login_form.data['active_code']
        # opt_code = request.session.get('opt_code')

        try:
            user = CustomerUser.objects.get(user_phone=user_phone)
            if user.is_active == False:
                # if code == opt_code:
                if user.check_password(login_form.data['password']):
                    user.is_active = True
                    # user.active_code = opt_code
                    user.save()
                    login(request, user)
                    messages.success(request, 'با موفقیت وارد شدید.')
                    return redirect('main:index')
                else:
                    messages.error(request, 'کلمه عبور اشتباه است.')
            # else:
            #     messages.error(request, 'کد وارد شده صحیح نمی باشد')
            else:
                messages.error(request, 'حساب کاربری شما قبلا فعال شده است')

        except CustomerUser.DoesNotExist:
            messages.error(request, 'کاربر مورد نظر با این شماره تلفن یافت نشد')
            context = {'form': login_form}
            return render(request, self.template_name, context)


class RegisterView(View):
    template_name = 'page/account/register.html'

    def get(self, request):
        register_form = RegisterForm()
        site_setting = SiteSettings.objects.all().first()
        social_media = SocialMedia.objects.all()
        context = {
            'form': register_form,
            'site_settings': site_setting,
            'social_media': social_media
        }
        return render(request, self.template_name, context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_phone = register_form.cleaned_data['user_phone']
            password = register_form.cleaned_data['password']
            name = register_form.cleaned_data['name']
            family = register_form.cleaned_data['family']
            user = CustomerUser.objects.filter(user_phone=user_phone).exists()
            if user:
                messages.error(request, 'شماره موبایل شما تکراری می باشد')

            else:
                CustomerUser.objects.create_user(
                    user_phone=user_phone,
                    name=name,
                    family=family,
                    password=password
                )
                messages.success(request, 'ثبت نام با موفقیت انجام شد')
                # opt_code = generate_random_number()
                # print(opt_code)
                # request.session['opt_code'] = opt_code
                # data = {'bodyId': 0000, 'to': f'{user_phone}', 'args': [str(opt_code)]}
                # response = requests.post('http://127.0.0.1:8000', json=data)
                return redirect('account:login')
        else:
            messages.error(request, 'فرم شما نامعتبر است')
        context = {
            'form': register_form
        }
        return render(request, self.template_name, context)


# class RecoveryPass(View):
#     template_name = 'page/account/recovery_pass.html'
#
#     def get(self, request, *args, **kwargs):
#         form = RecoveryPassForm()
#         site_setting = SiteSettings.objects.all().first()
#         social_media = SocialMedia.objects.all()
#         context = {
#             'form': form,
#             'site_settings': site_setting,
#             'social_media': social_media
#         }
#         return render(request, self.template_name, context)
#
#     def post(self, request, *args, **kwargs):
#         form = RecoveryPassForm(request.POST)
#         if form.is_valid():
#             user_phone = form.cleaned_data['user_phone']
#             request.session['user_phone'] = user_phone
#
#             user = CustomerUser.objects.filter(user_phone=user_phone).first()
#             if user:
#                 act_code = generate_random_number()
#                 request.session['act_code'] = act_code
#                 data = {'bodyId': 0000, 'to': f'{user_phone}', 'args': [str(act_code)]}
#                 response = requests.post('http://127.0.0.1:8000', json=data)
#                 messages.success(request, 'شماره موبایل شما با موفقیت پیدا شد')
#                 return redirect('account:active_code')
#             else:
#                 messages.error(request, 'شماره تلفن یافت نشد')
#                 return render(request, self.template_name, context={'form': form})
#         else:
#             messages.error(request, 'فرم نامعتبر است')
#             return render(request, self.template_name, context={'form': form})


# class ActiveCode(View):
#     template_name = 'page/account/active_code.html'
#
#     def get(self, request, *args, **kwargs):
#         form = ActiveCodeForm()
#         site_setting = SiteSettings.objects.all().first()
#         social_media = SocialMedia.objects.all()
#         context = {
#             'form': form,
#             'site_settings': site_setting,
#             'social_media': social_media
#         }
#
#         return render(request, self.template_name, context)
#
#     def post(self, request, *args, **kwargs):
#         form = ActiveCodeForm(request.POST)
#         user_phone = request.session.get('user_phone')
#         print(user_phone)
#         code = form.data['active_code']
#         act_code = request.session.get('act_code')
#
#         if code == act_code:
#             return redirect('account:change_pass')
#         else:
#             messages.error(request, 'کد معتبر نمی باشد')
#             return render(request, self.template_name, context={'form': form})


# class ChangePassView(View):
#     template_name = 'page/account/change_pass.html'
#
#     def get(self, request, *args, **kwargs):
#         form = ChangePasswordForm()
#         site_setting = SiteSettings.objects.all().first()
#         social_media = SocialMedia.objects.all()
#         context = {
#             'form': form,
#             'site_settings': site_setting,
#             'social_media': social_media
#         }
#         return render(request, self.template_name, context)
#
#     def post(self, request, *args, **kwargs):
#         form = ChangePasswordForm(request.POST)
#         user_phone = request.session.get('user_phone')
#         user = CustomerUser.objects.get(user_phone=user_phone)
#         if form.is_valid():
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             messages.success(request, 'رمز شما با موفقیت تغییر یافت')
#             return redirect('account:login')
#         else:
#             messages.error(request, 'فرم معتبر نمی باشد')
#             return render(request, self.template_name, context={'form': form})
