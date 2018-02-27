# This file has a command to allow user/app create user.
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from wger.core.models import UserProfile


class Command(BaseCommand):
    '''
    Helper command that helps the REST API create users
    '''

    def add_arguments(self, parser):
        parser.add_argument('username', nargs='?', type=str)

    def handle(self, **options):
        '''
        Checks whether the current the consumer can create users
        '''
        username = options.get("username", None)
        if username:
            try:
                userObject = User.objects.get(username=username)
                user = UserProfile.objects.get(user=userObject)
                if user.can_use_api_to_create_user:
                    return ('{} is already allowed to create users via the API'
                            .format(userObject.username))
                elif not user.can_use_api_to_create_user:
                    user.can_use_api_to_create_user = True
                    user.save()
                    return ('{}, you are now allowed to create users via the API'
                            .format(userObject.username))
            except:
                print('{} not yet registered.'.format(username))
        else:
            print('No username provided as an argument.')
