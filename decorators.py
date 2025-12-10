from django.shortcuts import redirect

def employee_login_required(view_func):
   
    def wrapper(request, *args, **kwargs):
        print("Decorator executed — session:", request.session.keys())
        if not request.session.get('employee_id'):
            return redirect('login')  
        return view_func(request, *args, **kwargs)
    return wrapper
