from django.urls import path
from .views import ArticleYearView, ArticleView, ArticleExtraView

urlpatterns = [
    path("", ArticleExtraView.as_view(), name="about_view"),
    path("<str:slug>", ArticleExtraView.as_view(), name="menu_view"),
    path("articles/", ArticleYearView.as_view(), name="articles"),
    path("articles/<int:year>/", ArticleYearView.as_view(), name="articles.by_year"),
    path(
        "articles/<int:year>/<int:month>/",
        ArticleYearView.as_view(),
        name="articles.by_month",
    ),
    path(
        "articles/<int:year>/<int:month>/<str:slug>",
        ArticleView.as_view(),
        name="article.detail",
    ),
]
