from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('home/', views.home, name='home'),
    path('clarity/', views.clarity_page, name='clarity'),
    path('capability/', views.capability_page, name='capability'),
    path('career/', views.career_page, name='career'),
    path('free-training/', views.free_training, name='free_training'),
    path('faqs/', views.faqs_page, name='faqs'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('smart-idea/', views.smart_idea_page, name='smart_idea'),
    path('expert-reviews/', views.expert_reviews, name='expert_reviews'),
]
