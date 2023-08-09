from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def cabinetView(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        request.session['language'] = language
    else:
        request.session['language'] = 'eng'
    user = request.user
    context = {
        'user': user,
        'this_url': 'cabinet_url',
    }
    return render(request, 'socialapp/cabinet_page.html', context)


def loginView(request):
    if request.method == 'GET':
        context = {
            'this_url': 'cabinet_url'
        }
        return render(request, 'socialapp/login.html', context)
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cabinet_url')


def testView(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        request.session['language'] = language
    if 'language' not in request.session.keys():
        request.session['language'] = 'eng'
    context = {
        'this_url': 'test_url',
    }
    return render(request, 'socialapp/test.html', context)


def view404(request, exception):
    return render(request, 'page_404.html', status=404)

