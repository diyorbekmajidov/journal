from django.urls import path
from .views import *

urlpatterns = [ 
    path('', IndexListView.as_view(), name='index_list'),
    
    path('category/<int:category_id>/', JournalCategoryView.as_view(), name='category'),
    path('journal/<int:pk>/', InfoSendJournalDetailView.as_view(), name='info'),
    path('journal_archive/<int:pk>/', ListJournalDetailView.as_view(), name='list'),


    path('list_art/<int:art_id>/', ArticlesListView.as_view(),name='list_art'),

    path('det_art/<int:pk>/', Detail_articlsDetView.as_view(), name='det_art'),


    # ===
    path('signin', sign_in, name='sign_in'),
    path('about', about, name='about'),
    path('course-list', course_l, name='course-list'),
    path('course', course, name='course'),
    path('course-detail', course_d, name='course-detail'),
    path('cart', cart, name='cart'),
    path('checkout', checkout, name='checkout'),
]

