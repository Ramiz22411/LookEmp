from django.views.generic import CreateView


class CreateViewWithCompany(CreateView):

    def form_valid(self, form):
        form.instance.company = self.request.user.company
        return super().form_valid(form)