from django.shortcuts import render_to_response
from django.template import RequestContext

from goals.forms import AddGoalForm
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


def new(request):
    new_goal_form = AddGoalForm()
    template_variables = {
        'form': new_goal_form
    }
    return render_response(request, "goals/new.html", template_variables)
