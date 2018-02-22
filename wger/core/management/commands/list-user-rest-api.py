# This file contains a command that lists all the users created
# by a specific user using the REST API.

from django.core.management.base import BaseCommand
from wger.core.models import UserProfile


class Command(BaseCommand):
    '''
    Helper admin command to list all the users created by a certain user
    '''

    def add_arguments(self, parser):
        parser.add_argument('username', nargs='?', type=str)

    def handle(self, **options):
        '''
        Check whether the current the consumer can create users
        '''
        username = options.get("username", None)

        if username:
            try:
                users = UserProfile.objects.all().filter(created_by=username)
                if len(users) < 1:
                    return 'No users created by {}'.format(username)

                elif len(users) > 0:
                    print('The users created by {} are: '.format(username))
                    for user in users:
                        print('\t' + user.user.username)
            except:
                print('{} not yet registered.'.format(username))
        else:
            print('No username provided as an arguement.')
