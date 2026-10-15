from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed


class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        # Lấy user_id từ token
        user_id = validated_token.get('user_id')
        if not user_id:
            raise AuthenticationFailed('User ID not found in token')

        # FIX M3: DummyUser đầy đủ pk/username/email
        class DummyUser:
            def __init__(self, id):
                self.id = id
                self.pk = id                    # ✅ DRF dùng pk
                self.username = f'user_{id}'    # ✅ cho str()
                self.email = ''
                self.first_name = ''
                self.last_name = ''
                self.is_authenticated = True
                self.is_active = True
                self.is_staff = False
                self.is_superuser = False

            def __str__(self):
                return f'DummyUser({self.id})'

            def get_full_name(self):
                return self.username

            def get_short_name(self):
                return self.username

        return DummyUser(user_id)