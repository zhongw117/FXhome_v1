# howdy/urls.py
from django.conf.urls import url
from howdy.views import homepage
from django.conf.urls import include
from django.views.generic import RedirectView
from . import views
from howdy import rentinglisting as rl
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', homepage),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
    url(r'^captcha', include('rest_captcha.urls')),
    # following is for user registration
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^rentingrooms', rl.rentingrooms, name='rentingrooms'),
    url(r'^newhomes', rl.newhomes, name='newhomes'),
    url(r'^hotel_image_form', views.hotel_image_view, name='hotel_image_form'),
    url(r'^success', views.success, name='success'),
    url(r'^hotel_images', views.display_hotel_images, name='hotel_images'),
    url(r'^mortgage_calculator', views.mortgage_calculator, name='mortgage_calculator'),
    url(r'^test', views.test, name='test'),
    url(r'^about', views.about, name='about'),
    url(r'^articlelist', rl.get_article, name='get_article'),
    url(r'^search_results', views.search, name='search')
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
