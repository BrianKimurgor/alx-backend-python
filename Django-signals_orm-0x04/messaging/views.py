from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def delete_user(request):
    """
    Allows a user to delete their account.
    """
    user = request.user
    user.delete()
    return JsonResponse({"message": "User account and related data deleted successfully."}, status=200)
