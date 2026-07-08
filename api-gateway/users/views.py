from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .permissions import IsAdmin

@method_decorator(csrf_exempt, name='dispatch')
class AssignRoleView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request):
        username = request.data.get('username')
        role = request.data.get('role')
        
        if role not in ['admin', 'teacher', 'student']:
            return Response({'error': 'Invalid role. Must be admin, teacher, or student'}, status=400)
        
        try:
            user = User.objects.get(username=username)
            user.profile.role = role
            user.profile.save()
            return Response({'message': f'Role updated to {role} for {username}'})
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)