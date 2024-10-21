from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from django_filters.views import FilterView
from social_network import filters

class UserListView(FilterView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'
    filterset_class = filters.UserFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.get_filterset(filters.UserFilter)
        return context

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user'

class UserCreateView(CreateView):
    model = User
    template_name = 'user_form.html'
    fields = ['first_name', 'last_name', 'email', 'avatar', 'date_of_birth']

class UserUpdateView(UpdateView):
    model = User
    template_name = 'user_form.html'
    fields = ['first_name', 'last_name', 'email', 'avatar', 'date_of_birth']

class UserDeleteView(DeleteView):
    model = User
    template_name = 'user_confirm_delete.html'
    success_url = reverse_lazy('user_list')

# class MessageListView(ListView):
#     model = Message
#     template_name = 'message_list.html'
#     context_object_name = 'messages'
#
# class MessageDetailView(DetailView):
#     model = Message
#     template_name = 'message_detail.html'
#     context_object_name = 'message'
#
# class MessageCreateView(CreateView):
#     model = Message
#     template_name = 'message_form.html'
#     fields = ['text_message', 'sender', 'receiver']
#
# class MessageUpdateView(UpdateView):
#     model = Message
#     template_name = 'message_form.html'
#     fields = ['text_message', 'sender', 'receiver']
#
# class MessageDeleteView(DeleteView):
#     model = Message
#     template_name = 'message_confirm_delete.html'
#     success_url = reverse_lazy('message_list')
