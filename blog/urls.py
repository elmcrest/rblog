from django.urls import path
from .views import ArticleYearView, ArticleView

urlpatterns = [
    path("<int:year>/", ArticleYearView.as_view(), name="articles.year"),
    path("<int:year>/<int:pk>", ArticleView.as_view(), name="article.detail"),
]
