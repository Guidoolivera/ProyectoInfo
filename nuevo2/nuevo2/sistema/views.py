from django.views.generic import TemplateView

#def index(request):
#    return render(request, 'index.html')

class IndexView(TemplateView):
    template_name = 'index.html'