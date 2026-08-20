from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed

class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        # Lấy user_id từ token
        user_id = validated_token.get('user_id')
        if not user_id:
            raise AuthenticationFailed('User ID not found in token')
        # Tạo một đối tượng user ảo để DRF coi như đã xác thực
        class DummyUser:
            def __init__(self, id):
                self.id = id
                self.is_authenticated = True
                self.is_active = True
            def __str__(self):
                return f'DummyUser({self.id})'
        return DummyUser(user_id)