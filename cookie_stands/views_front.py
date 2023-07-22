from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import CookieStand


class CookieStandListView(LoginRequiredMixin, ListView):
    template_name = "CookieStand/CookieStand_list.html"
    model = CookieStand
    context_object_name = "CookieStand"


class CookieStandDetailView(LoginRequiredMixin, DetailView):
    template_name = "CookieStand/CookieStand_detail.html"
    model = CookieStand


class CookieStandUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "CookieStand/CookieStand_update.html"
    model = CookieStand
    fields = "__all__"


class CookieStandCreateView(LoginRequiredMixin, CreateView):
    template_name = "CookieStand/CookieStand_create.html"
    model = CookieStand
    fields = ["location", "average_cookies_per_sale", "owner"]

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CookieStandDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "CookieStand/CookieStand_delete.html"
    model = CookieStand
    success_url = reverse_lazy("CookieStand_list")
