  
from django.urls import path
from . import views


urlpatterns = [

	#path('article/', views.articleList, name="articless"),
	#path('detail/<int:pk>/', views.articleDetail, name="articless"),
	path('article/', views.ArticleAPIView.as_view(), name="articless"),
	path('detail/<int:id>/', views.articleDetail.as_view(), name="articless"),
]
