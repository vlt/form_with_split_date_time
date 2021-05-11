from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .forms import (
    UniverseForm,
)

from .models import (
    Universe,
)


class IndexView(ListView):
    model = Universe


class UniverseCreate(CreateView):
    model = Universe
    form_class = UniverseForm
    success_url = reverse_lazy("index")
