from django.shortcuts import render


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
