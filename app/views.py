from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Contact
from django.contrib.auth.decorators import login_required


class HomeView(LoginRequiredMixin, ListView):
    template_name = "index.html"
    model = Contact
    context_object_name = "contacts"

    # filtering the data that belongs to the LogIn user ..
    def get_queryset(self):
        contacts = super().get_queryset()
        return contacts.filter(manager=self.request.user)


class ContactDetailView(LoginRequiredMixin, DetailView):
    template_name = "detail.html"
    model = Contact
    context_object_name = "contact"


@login_required
def search(request):
    if request.GET:
        search_term = request.GET['search']
        search_result = Contact.objects.filter(
            Q(name__icontains=search_term) |
            Q(email__icontains=search_term) |
            Q(info__icontains=search_term) |
            Q(phone__iexact=search_term)
        )
    context = {
        'search_term': search_term,
        'contacts': search_result.filter(manager=request.user)
    }
    return render(request, "search.html", context)


class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    template_name = "create.html"
    fields = ['name', 'email', 'phone', 'info', 'gender', 'image']

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.manager = self.request.user
        instance.save()
        messages.success(self.request, "Contact created successfully ....!")
        return redirect('home')


class ContactUpdateView(LoginRequiredMixin, UpdateView):
    model = Contact
    template_name = "update.html"
    fields = ['name', 'email', 'phone', 'info', 'gender', 'image']

    def form_valid(self, form):
        instance = form.save()
        messages.success(self.request, "Contact has been updated....")
        return redirect('detail', instance.pk)


class ContactDeleteView(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = "delete.html"
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "The contact has been successfully deleted...")
        return super().delete(self, request, *args, **kwargs)


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("home")
