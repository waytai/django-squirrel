from django import forms

from goals.models import Goal

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div


class AddGoalForm(forms.Form):

    name = forms.CharField(max_length=50)
    specific_target = forms.BooleanField(label="I have a specific target amount in mind")
    target_amount = forms.IntegerField()
    starting_amount = forms.IntegerField(initial=0)
    target_date = forms.DateField()
    regular_payins = forms.BooleanField(label="I want to make regular contributions")
    period = forms.ChoiceField(choices=Goal.PERIOD_CHOICES)
    step = forms.IntegerField(initial=1)
    increment = forms.IntegerField(initial=100)

    def __init__(self, *args, **kwargs):
        super(AddGoalForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Add a new goal',
                Div(
                    'name',
                    'specific_target',
                ),
                Div(
                    'target_amount',
                    'target_date',
                    css_class="hidden",
                    id="target",
                ),
                Div(
                    'starting_amount',
                    'regular_payins',
                ),
                Div(
                    'period',
                    'step',
                    'increment',
                    css_class="hidden",
                    id="repeat",
                )
            ),
            ButtonHolder(
                Submit('submit', 'Save Goal', css_class='btn btn-success')
            )
        )
