from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from goals.forms import AddGoalForm
from goals.models import Goal
from goals.queries import get_goals_by_user


def render_response(req, *args, **kwargs):
    kwargs['context_instance'] = RequestContext(req)
    return render_to_response(*args, **kwargs)


@login_required
def dashboard(request):
    pass


@login_required
def home(request):
    goals = get_goals_by_user(request.user.id)
    template_variables = {
        'goals': goals
    }
    return render_response(request, "goals/list.html", template_variables)


@login_required
def new(request):
    if request.POST:
        new_goal_form = AddGoalForm(request.POST)
        if new_goal_form.is_valid():
            goal = Goal()
            goal.created_by = request.user
            goal.modified_by = request.user
            goal.user = request.user
            goal.name = new_goal_form.cleaned_data['name']
            if new_goal_form.cleaned_data['specific_target'] is True:
                goal.target_amount = new_goal_form.cleaned_data['target_amount']
                goal.target_date = new_goal_form.cleaned_data['target_date']
            if new_goal_form.cleaned_data['regular_payins'] is True:
                goal.period = new_goal_form.cleaned_data['period']
                goal.period_step = new_goal_form.cleaned_data['step']
                goal.period_increment = new_goal_form.cleaned_data['increment']
            goal.status = 2 if new_goal_form.cleaned_data['regular_payins'] is True else 0
            goal.save()
            return redirect('goals_home')
    else:
        new_goal_form = AddGoalForm()
    template_variables = {
        'form': new_goal_form
    }
    return render_response(request, "goals/new.html", template_variables)
