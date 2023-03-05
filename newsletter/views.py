from django.shortcuts import render
from .forms import NewsletterSignUpForm
from django.views.generic import TemplateView
from newsletter.forms import NewsletterSignUpForm


def newsletter_signup(request):
    form = NewsletterSignUpForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # Add logic to handle successful sign-up (e.g. redirect to a thank-you page)  # noqa
    return render(request, 'newsletter/signup.html', {'form': form})  # noqa


class BaseView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newsletter_signup_form'] = NewsletterSignUpForm()
        return context
