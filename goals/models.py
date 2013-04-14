from django.db import models
from django.contrib.auth.models import User


class Goal(models.Model):

    STATUS_CHOICES = (
        (0, 'Inactive'),
        (1, 'Achieved'),
        (2, 'Ongoing'),
    )

    created_date = models.DateTimeField()
    created_by = models.ForeignKey(User, related_name="+")
    user = models.ForeignKey(User, related_name="goals")
    end_amount = models.IntegerField(null=True)
    current_amount = models.IntegerField()
    target_date = models.DateField(null=True)
    status = models.SmallIntegerField(choices=STATUS_CHOICES)
