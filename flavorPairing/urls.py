#root urls

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$', 'flavorPairingProject.views.login'),


    #admin
    url(r'^admin/', include(admin.site.urls)),

    #user account
    url(r'^accounts/login/$', 'flavorPairing.views.login'),
    url(r'^accounts/auth/$', 'flavorPairing.views.auth_view'),
    url(r'^accounts/logout/$', 'flavorPairing.views.logout'),
    url(r'^accounts/loggedin/$', 'flavorPairing.views.loggedin'),
    url(r'^accounts/invalid/$', 'flavorPairing.views.invalid_login'),

)
