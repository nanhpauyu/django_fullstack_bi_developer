from django.shortcuts import redirect


def login_required(func):
    def wrapper(request, *args, **kwargs):
        if 'user' in request.session:
            return func(request, *args, **kwargs)
        else:
            return redirect('login')

    return wrapper