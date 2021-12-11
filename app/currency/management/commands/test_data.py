import random

from django.core.management.base import BaseCommand
from currency.models import Rate, Source
from currency import model_choices as mch


class Command(BaseCommand):
    help = 'Generate dummy data'

    def handle(self, *args, **options):
        for i in range(4):
            if not Source.objects.filter(code_name=str(i)).exists():
                Source.objects.create(name=str(i), code_name=str(i))

        for index in range(400):
            Rate.objects.create(
                buy=random.randint(20, 40),
                sale=random.randint(20, 40),
                type=random.choice(mch.RateTypeChoices.choices)[0],
                source=Source.objects.order_by('?').last(),
            )
