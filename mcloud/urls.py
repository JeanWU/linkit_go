from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^contact$', 'app.views.contact', name='contact'),
    url(r'^humanflow/$','app.views.humanflow', name='humanflow'),
    url(r'^about', 'app.views.about', name='about'),
    url(r'^showyoutube/$', 'app.views.showyoutube', name='showyoutube'),
    url(r'^showppt/$', 'app.views.showppt', name='showppt'),
    url(r'^dynamic_information/$', 'app.views.dynamic_information', name='dynamic_information'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),
    #url(r'^T1LL/$', 'app.views.T1LL_input', name='T1LL_input'),
    #url(r'^T1LL_result/$', 'app.views.T1LL_result', name='T1LL_result'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    ) 
