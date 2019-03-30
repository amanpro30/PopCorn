from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views as core_views
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('landing', core_views.landing, name='landing'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('', TemplateView.as_view(template_name='html/basehome.html'), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/', include('registration.urls'))
]
