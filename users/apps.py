from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = 'users'

    # below piece of code is needed for automatic profile creation for user
    def ready(self):
        import users.signals
