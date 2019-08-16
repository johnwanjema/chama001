from django.urls import path, include, re_path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', views.homepage, name='home'),
    # path('daraja/stk-push', views.stk_push_callback, name='mpesa_stk_push_callback'),
    path('register/', views.signup, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('chama/create/', views.ChamaCreate.as_view(), name='create-chama'),
    path('chama/<uuid:pk>', views.ChamaDetailView.as_view(), name='chama_detail'),
    path('<uuid:pk>/addmember', views.ChamaAddMember, name='add-member'),
    path('<uuid:pk>/remove_member/<phone_number>', views.ChamaRemoveMember, name='remove-member'),
    path('mychamas/', views.CurrentUserChamas.as_view(), name="my-chamas"),
    path('<uuid:pk>/makepayment/', views.TransactionCreate.as_view(), name='pay'),
        
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
