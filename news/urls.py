from django.urls import path
from .views import home,get_category,view_news

urlpatterns=[

	path('',home,name='home'),
	path('category/<int:category_id>/', get_category, name='category'),
	path('news/<int:news_id>/',view_news,name='view_news'),
	

]