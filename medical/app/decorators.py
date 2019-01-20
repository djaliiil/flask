from functools import wraps

from flask import abort
from flask_login import current_user

from app.models.user import Permission


def permission_required(permission):
    """Restrict a view to users with the given permission."""

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            print(current_user.role_id)
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)

        return decorated_function

    return decorator

 
def patient_required(f):
    return permission_required(Permission.EDIT_PROFILE)(f)
def doctor_required(f):
    return permission_required(Permission.WRITE_DIAGNOSIS)(f)
def admin_required(f):
    return permission_required(Permission.WRITE_DIAGNOSIS)(f)
 