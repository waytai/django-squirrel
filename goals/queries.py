from goals.models import Goal


def get_goals_by_user(user_id):
    return Goal.objects.filter(user__id=user_id)
