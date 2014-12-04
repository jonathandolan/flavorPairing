from django.conf.urls import patterns, include, url
from django.contrib import admin
from flavorPairing.views import IngredientCreate
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

urlpatterns = patterns('',

    #url(r'^$', 'flavorPairing.views.login'),

    url(r'^admin/', include(admin.site.urls)),

    #user account
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    #url(r'^accounts/login/$', 'flavorPairing.views.login'),
    url(r"^account/", include("account.urls")),
    url(r'^accounts/auth/$', 'flavorPairing.views.auth_view'),
    url(r'^accounts/logout/$', 'flavorPairing.views.logout'),
    url(r'^accounts/loggedin/$', 'flavorPairing.views.loggedin'),
    url(r'^accounts/invalid/$', 'flavorPairing.views.invalid_login'),
    url(r'^createIngredient/$', 'flavorPairing.views.IngredientCreate'),
    url(r'ingredient/add/$', IngredientCreate.as_view(), name='ingredient_add'),
)

urlpatterns += staticfiles_urlpatterns()
