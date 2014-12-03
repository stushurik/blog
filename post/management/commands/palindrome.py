from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        tested_str = unicode(args[0].decode('utf-8'))
        middle = len(tested_str) / 2

        first_part = tested_str[:middle]

        if len(tested_str) % 2:
            second_part = tested_str[middle + 1:]
        else:
            second_part = tested_str[middle:]

        print first_part.upper() == second_part[::-1].upper()