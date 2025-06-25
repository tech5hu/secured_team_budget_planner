from django.contrib import messages
from django.shortcuts import redirect

# custom decorator checks if a user is logged in and is a staff (admin) user 
def staff_required(view_func):
    # function that wraps around the original view
    def _wrapped_view(request, *args, **kwargs):
        # check if the user is logged in
        if request.user.is_authenticated:
            # check if the user has staff permissions (admin)
            if request.user.is_staff:
                # if they are staff, allow access to the original view
                return view_func(request, *args, **kwargs)
            else:
                # if logged in but not staff, show an error and send them to the dashboard
                # this message must match exactly what your test looks for
                messages.error(request, "You do not have permission to view this page.")
                return redirect('dashboard')  
        else:
            # if not logged in at all, show error and send to login page
            # this ensures unauthenticated users can't access staff-only views
            messages.error(request, "Please log in to access this page.")
            return redirect('login')

    # returning the custom logic to wrap around a view
    return _wrapped_view
