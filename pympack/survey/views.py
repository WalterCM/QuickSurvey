from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from.models import Survey
from .forms import SurveyForm, UserRegistrationForm
from .services import get_categories

def survey(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            print("saving form")
            return HttpResponseRedirect('thanks')
        else:
            print("not valid")
    else:
        form = SurveyForm()
    #print|(form)
    return render(request, 'survey/survey.html', {'form': form})

def thanks(request):
    return render(request, 'survey/thanks.html')

def results(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('../../accounts/login/')

    results = []
    for category in get_categories():
        results.append({"category":category[1], "count":Survey.objects.filter(category=category[0]).count()})

    return render(request, 'survey/results.html', {'section': 'dashboard', 'results':results})

@login_required
def details(request):
    details = Survey.objects.all()
    paginator = Paginator(details, 3) # 3 items por cada pagina
    page = request.GET.get('page')
    try:
        details = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        details = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        details = paginator.page(paginator.num_pages)

    return render(request, 'survey/details.html', {'page': page, 'details':details})

class SurveyEditView(UpdateView):
    model = Survey
    form_class = SurveyForm
    template_name = 'survey/survey.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('../../edited')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(SurveyEditView, self).dispatch(request, *args, **kwargs)

@login_required
def edited(request):
    return render(request, 'survey/edited.html')

class SurveyDeleteView(DeleteView):
   model = Survey

   def get_success_url(self):
      return reverse('details')

   @method_decorator(login_required)
   def dispatch(self, request, *args, **kwargs):
      return super(SurveyDeleteView, self).dispatch(request, *args, **kwargs)

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})
