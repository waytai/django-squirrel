from django.shortcuts import render_to_response
from django.template import RequestContext

from goals.queries import get_goals_by_user


def render_response(req, *args, **kwargs):
    kwargs['context_instance'] = RequestContext(req)
    return render_to_response(*args, **kwargs)


def dashboard(request):
    pass


def home(request):
    goals = get_goals_by_user(request.user.id)
    template_variables = {
        'goals': goals
    }
    return render_response(request, "goals/list.html", template_variables)
