from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Management command for creating a superuser.
    """

    def handle(self, *args, **options):
        """
        Handle the command execution.

        Args:
            args: Command line arguments.
            options: Command options.

        """

        user = User.objects.create(
            email='enter_your_email',
            first_name='enter_your_first_name',
            last_name='enter_your_last_name',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('enter_your_password')
        user.save()
