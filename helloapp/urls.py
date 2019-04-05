"""helloapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from howdy import views as webViews
from howdy import rentinglisting as rl
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('howdy.urls')),
    path('about', webViews.about, name='about'),
    path('post', webViews.post, name='post'),
    path('login/', webViews.login, name='login'),
    path('logout/', webViews.logout, 'logout'),


    re_path(r'^useradmin/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'', include(wagtail_urls)),  # base location from where the pages of your Wagtail site will be served
    # path('client/signup/createAccount/', clientView.createAccount, name='client-createAccount'),
    # path('client/login/', clientView.loginPage, name='client-login'),
    # path('client/signup/', clientView.signupPage, name='client-signup'),
    # path('client/login/verify/', clientView.loginVerify, name='client-loginVerify'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
