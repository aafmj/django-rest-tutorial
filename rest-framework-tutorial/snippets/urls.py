from django.conf.urls import include, url
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from snippets import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url('openapi/', TemplateView.as_view(template_name="index.html")),
    url(r'^', include(router.urls))
]
