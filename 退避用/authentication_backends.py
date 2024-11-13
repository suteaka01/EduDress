# authentication_backends.py
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class NicknameAuthBackend(ModelBackend):
    def authenticate(self, request, nickname=None, password=None, **kwargs):
        try:
            user = User.objects.get(nickname=nickname)  # ユーザーをニックネームで取得
            if user.check_password(password):  # パスワードが一致するか確認
                return user
        except User.DoesNotExist:
            return None  # 該当するユーザーが存在しない場合
