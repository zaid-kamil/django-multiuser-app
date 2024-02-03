from functools import wraps
from django.shortcuts import redirect

def user_in_group_required(groups):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            # Check if the user is in any of the specified groups
            if any(request.user.groups.filter(name=group).exists() for group in groups):
                return view_func(request, *args, **kwargs)
            else:
                # Redirect to some unauthorized access page or take appropriate action
                return redirect('unauthorized_access')
        
        return wrapper
    return decorator