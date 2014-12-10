from django.conf.urls import patterns, include, url
from django.contrib import admin
from flavorPairing.views import IngredientListView, PairListView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView, ListView

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^account/", include("account.urls")),
    url(r'^accounts/auth/$', 'flavorPairing.views.auth_view'),
    url(r'^accounts/logout/$', 'flavorPairing.views.logout'),
    url(r'^accounts/loggedin/$', 'flavorPairing.views.loggedin'),
    url(r'^accounts/invalid/$', 'flavorPairing.views.invalid_login'),
    url(r'ingredient/add/$', 'flavorPairing.views.get_ing_name', name='ingredient_add'),
    url(r'^ingredient-list/$', IngredientListView.as_view(), name='ingredient_list'),
    url(r'^pair-list/$', PairListView.as_view(), name='pair_list'),
    url(r'^pair/add/$', 'flavorPairing.views.get_pair', name='pair_add'),
    url(r'^pair/find/$', 'flavorPairing.views.find_pairings', name='find_pair'),
)

urlpatterns += staticfiles_urlpatterns()
