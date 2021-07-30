from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class OtherPageView(TemplateView):
    template_name = 'other.html'

class MyPageView(TemplateView):
    template_name = 'mypage.html'