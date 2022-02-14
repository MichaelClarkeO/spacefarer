from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.shortcuts import render
from .models import Planet
from django.views import View 
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView

class Home(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"


class Index(TemplateView):
    template_name = "index.html"


@method_decorator(login_required, name='dispatch')
class WayfarerList(TemplateView):
    template_name = "Wayfarer_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["planets"] = Planet.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["planets"] = Planet.objects.all()
            context["header"] = "Trending Planets"
        return context

class WayfarerCreate(CreateView):
    model = Planet
    fields = ['name', 'img', 'bio']
    template_name = "wayfarer_create.html"
    success_url = "/wayfarers/"

class WayfarerDetail(DetailView):
    model = Planet
    template_name = "Wayfarer_detail.html"

class WayfarerUpdate(UpdateView):
    model = Planet
    fields = ['name', 'img', 'bio',]
    template_name = "wayfarer_update.html"
    success_url = "/wayfarers/"
   
class WayfarerDelete(DeleteView):
    model = Planet
    template_name = "wayfarer_delete_confirmation.html"
    success_url = "/wayfarers/"

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("wayfarer_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
