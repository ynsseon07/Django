from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.db import IntegrityError

from random import *
from .models import *
from sendEmail.views import *
import hashlib

# Create your views here.
def index(request):
    if 'user_name' in request.session.keys():
        return render(request, 'main/index.html', content)
    else:
        return redirect('main_signin')

# 회원가입 페이지
def signup(request):
    return render(request, 'main/signup.html')


def join(request):
    print(request)
    name = request.POST['signupName']
    email = request.POST['signupEmail']
    pw = request.POST['signupPW']

    if len(email) >= 200:
        message = '입력하신 이메일이 너무 길어요.'
        return render(request, 'main/error.html', {"message": message})
    if len(name) >= 30:
        message = '입력하신 이름이 너무 길어요.'
        return render(request, 'main/error.html', {"message": message})

    try :
        # pw encryption
        encoded_pw = pw.encode()
        encrypted_pw = hashlib.sha256(encoded_pw).hexdigest()
        user = User(user_name = name, user_email = email, user_password = encrypted_pw)
        user.save()
        code = randint(1000, 9999)
        response = redirect('main_verifyCode')
        
        response.set_cookie('code',code)
        response.set_cookie('user_id',user.id)
        
        # 이메일 발송 함수 호출
        send_result = send(email,code)
        print('send_result=', send_result)
        if send_result:
            return response
        else:
            content = {'message':'이메일 발송에 실패하였습니다.'}
            return render(request, 'main/error.html', content)
            # return HttpResponse("이메일 발송에 실패하였습니다.")

    # 중복된 이메일로 가입 시
    except IntegrityError:
        message = '이미 존재하는 이메일입니다.'
        return render(request, 'main/error.html', {"message": message})

    # 알 수 없는 오류 발생시
    except:
        message = '알 수 없는 오류가 발생했습니다.'
        return render(request, 'main/error.html', {"message": message})

# 로그인 페이지
def signin(request):
    return render(request, 'main/signin.html')   


def login(request):
    loginEmail = request.POST['loginEmail']
    loginPW = request.POST['loginPW']
    try:
        user = User.objects.get(user_email = loginEmail)
    except:
        return redirect('main_loginFail')

    # 사용자가 입력한 PW 암호화
    encoded_loginPW = loginPW.encode()
    encrypted_loginPW = hashlib.sha256(encoded_loginPW).hexdigest()

    # 사용자 이름과 이메일 session에 저장
    if user.user_password == encrypted_loginPW:
        request.session['user_name'] = user.user_name
        request.session['user_email'] = user.user_email
        return redirect('main_index')
    else:
        return redirect('main_loginFail')


def loginFail(request):
    return render(request, 'main/loginFail.html') 


def logout(request):
    del request.session['user_name']
    del request.session['user_email']
    return redirect('main_signin')

# 이메일 인증코드 입력 화면
def verifyCode(request):
    return render(request, 'main/verifyCode.html')

# 이메일 인증 완료시 admin 페이지에서 User validate에 체크가 됨
# 이메일 인증 완료시 index.html 화면 표시
def verify(request):
    user_code = request.POST['verifyCode']
    cookie_code = request.COOKIES.get('code')
    if user_code == cookie_code:
        user = User.objects.get(id = request.COOKIES.get('user_id'))
        user.user_validate = 1  # User validate 체크박스에 체크표시
        user.save()
        response = redirect('main_index')
        response.delete_cookie('code')
        response.delete_cookie('user_id')
        # response.set_cookie('user',user)
        request.session['user_name'] = user.user_name
        request.session['user_email'] = user.user_email
        return response
    else:
        redirect('main_verifyCode')


def result(request):
    if 'user_name' in request.session.keys():
        content = {}
        content['grade_calculate_dic'] = request.session['grade_calculate_dic']
        content['email_domain_dic'] = request.session['email_domain_dic']
        del request.session['grade_calculate_dic']
        del request.session['email_domain_dic']
        return render(request, 'main/result.html',content)
    else:
        return redirect('main_signin')
