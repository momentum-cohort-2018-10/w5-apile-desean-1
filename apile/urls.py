from django.contrib import admin
from django.urls import path, include
from linkinator import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.generic import TemplateView, RedirectView
from django.conf import settings
from django.contrib.auth.views import (
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView,
)

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('post/<slug>', views.post_detail, name='post_detail'),
    path('post/<slug>/add_comment_to_post', views.add_comment_to_post,
         name="add_comment_to_post"),
    path('post/<slug>/<pk>/edit_comment', views.edit_comment, name='edit_comment'),
    path('post/<slug>/<pk>/delete_comment', views.delete_comment, name='delete_comment'),
    path('post/<slug>/vote', views.vote_detail, name='vote_detail'),
    path('search', views.search, name='search'),
    path('vote_index/<slug>', views.vote_index, name='vote_index'),
    path('<request.user>/voted', views.voted, name='voted'),
    path('<request.user>/posted', views.posted, name='posted'),
    path('<request.user>/commented', views.commented, name='commented'),
    path('create_post', views.create_post, name='create_post'),
    path('post/<slug>/edit_post', views.edit_post, name='edit_post'),
    # account registration views
    path('accounts/password/reset/', PasswordResetView.as_view(
        template_name='registration/password_reset_form.html'), name="password_reset"),
    path('accounts/password/reset/done/', PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'), name="password_reset_done"),
    path('accounts/password/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'), name="password_reset_confirm"),
    path('accounts/password/done/', PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'), name="password_reset_complete"),
    path('accounts/', include('registration.backends.simple.urls')),
    path('admin/', admin.site.urls),
    # path(r'^post/(?P<pk>\d+)/comment/$',
    #      views.add_comment_to_post, name='add_comment_to_post'),



]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
