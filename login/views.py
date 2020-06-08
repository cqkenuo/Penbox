from django.shortcuts import render,redirect
from . import models
from . import forms
import hashlib

def hash_code(s, salt='mysite'):# 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.session.get('is_login', None):  # 不允许重复登录
        return redirect('/')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            try:
                user = models.User.objects.get(username=username)
            except :
                message = '用户不存在！'
                return render(request, 'login.html', locals())

            if user.password == hash_code(password):
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.username
                next = request.GET.get('next')
                if next:
                    return redirect(next)
                else:
                    return redirect('/')
            else:
                message = '密码不正确！'
                return render(request, 'login.html', locals())
        else:
            return render(request, 'login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login.html', locals())

def changepwd(request):
    if request.method == 'POST':
        change_pwd_form = forms.ChangePwdForm(request.POST)
        message = '请检查填写的内容！'
        if change_pwd_form.is_valid():
            old_password = change_pwd_form.cleaned_data.get('old_password')
            new_password = change_pwd_form.cleaned_data.get('new_password')
            user = models.User.objects.get(username=request.session["user_name"])
            if user.password == hash_code(old_password):
                user.password = hash_code(new_password)
                user.save()
                return redirect('/')
            else:
                message = '原密码不正确！'
                return render(request, 'changepwd.html', locals())
        else:
            return render(request, 'changepwd.html', locals())

    change_pwd_form = forms.ChangePwdForm()
    return render(request, 'changepwd.html', locals())

def logout(request):
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/login/")