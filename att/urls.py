from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from recipes.views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$', RecipeCreateView.as_view(), name='recipe_create'),
    url(r'^recipe/(?P<pk>\d+)/$', RecipeDetailView.as_view(), name='recipe_detail'),
    
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

# https://docs.djangoproject.com/en/1.5/ref/contrib/staticfiles/#django.contrib.staticfiles.views.serve
# from django.conf import settings
#
# if settings.DEBUG:
#     urlpatterns += patterns('django.contrib.staticfiles.views',
#         url(r'^static/(?P<path>.*)$', 'serve'),
#     )

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()