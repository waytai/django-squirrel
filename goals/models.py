from django.db import models
from django.contrib.auth.models import User


class Goal(models.Model):

    STATUS_CHOICES = (
        (0, 'Manual'),  # savings entered manually
        (1, 'Achieved'),  # target reached
        (2, 'Ongoing'),  # specific amount saved over recurring period
    )

    PERIOD_CHOICES = (
        (1, "Day"),
        (2, "Week"),
        (3, "Fortnight"),
        (4, "Month"),
        (5, "Quarter"),
        (6, "Year"),
    )

    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="+")
    modified_date = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, related_name="+")
    user = models.ForeignKey(User, related_name="goals")
    name = models.CharField(max_length=50)
    target_amount = models.IntegerField(null=True, blank=True)
    current_amount = models.IntegerField(default=0)
    target_date = models.DateField(null=True, blank=True)
    status = models.SmallIntegerField(choices=STATUS_CHOICES)

    period = models.SmallIntegerField(choices=PERIOD_CHOICES, null=True, blank=True, default=4)
    period_step = models.SmallIntegerField(null=True, blank=True, default=1)
    period_increment = models.IntegerField(null=True, blank=True, default=100)

    def clean(self):
        from django.core.exceptions import ValidationError
        # Validation for ongoing goals
        if self.status == 2:
            # period is required
            if self.period is None:
                raise ValidationError("A value for Period must be selected.")
            # period step is required
            if self.period_step is None:
                raise ValidationError("A value for Period Step must be selected.")
            # period increment is required
            if self.period_increment is None:
                raise ValidationError("A value for Period Increment must be selected.")
            # period increment cannot be zero
            if self.period_increment == 0:
                raise ValidationError("The period increment cannot be zero.")

    def __unicode__(self):
        return "%s: %s" % (self.name, self.target_amount if self.target_amount is not None else "Unlimited")


class Transaction(models.Model):

    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)
    goal = models.ForeignKey(Goal)
    pay_in = models.BooleanField(default=True)
    amount = models.IntegerField(null=False)

    def clean(self):
        from django.core.exceptions import ValidationError
        # payin - amount cannot be negative
        if self.pay_in is True and self.amount < 0:
            raise ValidationError("Amount must be positive for a pay in.")
        # payout - amount cannot be positive
        if self.pay_in is False and self.amount > 0:
            raise ValidationError("Amount must be negative for a pay out.")

    def __unicode__(self):
        return self.amount
