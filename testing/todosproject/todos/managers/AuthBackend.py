from django.contrib.auth.backends import ModelBackend


class CustomBackend(ModelBackend):
    def authenticate(self, email=None, password=None, **kwargs):
        pass

    def get_user(self, user_id):
        pass
