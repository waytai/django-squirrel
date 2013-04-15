from django.db import models
from django.contrib.auth.models import User


class Goal(models.Model):

    STATUS_CHOICES = (
        (0, 'Inactive'),  # savings entered manually
        (1, 'Achieved'),  # target reached
        (2, 'Ongoing'),  # specific amount saved over recurring period
    )

    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="+")
    modified_date = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, related_name="+")
    user = models.ForeignKey(User, related_name="goals")
    name = models.CharField(max_length=50)
    end_amount = models.IntegerField(null=True, blank=True)
    current_amount = models.IntegerField(default=0)
    target_date = models.DateField(null=True, blank=True)
    status = models.SmallIntegerField(choices=STATUS_CHOICES)
