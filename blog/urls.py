from django.urls import path
from .views import ArticleListView, ArticleView, ArticleExtraView, ArticleSearchApi

urlpatterns = [
    path("", ArticleExtraView.as_view(), name="about_view"),
    path("<str:slug>", ArticleExtraView.as_view(), name="menu_view"),
    path("articles/", ArticleListView.as_view(), name="articles"),
    path("articles/<int:year>/", ArticleListView.as_view(), name="articles.by_year"),
    path(
        "articles/<int:year>/<int:month>/",
        ArticleListView.as_view(),
        name="articles.by_month",
    ),
    path(
        "articles/<int:year>/<int:month>/<str:slug>",
        ArticleView.as_view(),
        name="article.detail",
    ),
    path("articles/tag/<str:tag>", ArticleListView.as_view(), name="articles.by_tag"),
    path("articles/search", ArticleSearchApi.as_view(), name="articles.search"),
]
