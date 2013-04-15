from django.contrib import admin
from goals.models import Goal, Transaction


class TransactionInline(admin.TabularInline):
    model = Transaction
    extra = 1


class GoalAdmin(admin.ModelAdmin):
    inlines = [
        TransactionInline
    ]


admin.site.register(Goal, GoalAdmin)
