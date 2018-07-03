from django.urls import path
from .views import ArticleYearView

urlpatterns = [path("<int:year>/", ArticleYearView.as_view(), name="articles.year")]
