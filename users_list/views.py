# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from users_list.models import UserProfile
from users_list.forms import UserForm


class IndexView(generic.ListView):
    model = UserProfile
    template_name = 'index.html'


class UserView(generic.DetailView):
    model = User
    template_name = 'user_details.html'


class CreateUserView(generic.CreateView):
    model = User
    template_name = 'create_update_user.html'
    form_class = UserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        self.object = form.save()

        user_profile = UserProfile(
            user=self.object,
            birthday=form.data.get('birthday', None)
        )
        user_profile.save()

        return HttpResponseRedirect(self.get_success_url())


class UpdateUserView(generic.UpdateView):
    model = User
    template_name = 'create_update_user.html'
    form_class = UserForm
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        self.object = get_object_or_404(User, pk=kwargs['pk'])

        user_profile = get_object_or_404(UserProfile, user=self.object)
        form = self.get_form(UserForm)
        form.initial['birthday'] = user_profile.birthday

        return self.render_to_response(
            self.get_context_data(form=form,)
        )

    def form_valid(self, form):
        self.object = form.save()

        user_profile = get_object_or_404(UserProfile, user=self.object)
        user_profile.birthday = form.data.get('birthday', None)
        user_profile.save()

        return HttpResponseRedirect(self.get_success_url())


class DeleteUserView(generic.DeleteView):
    model = User
    template_name = 'delete_user.html'
    success_url = reverse_lazy('index')
