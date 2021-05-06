from django.urls import path
from blog.views import views, post_views, comment_views

app_name = 'blog'

urlpatterns = [
    path('', post_views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/<int:pk>', post_views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', post_views.PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', post_views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/remove/', post_views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/publish/', post_views.post_publish, name='post_publish'),
    path('drafts/', post_views.DraftListView.as_view(), name='draft_list'),
    path('post/<int:pk>/comment/', comment_views.comment_add, name='comment_add'),
    path('comment/<int:pk>/approve/', comment_views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove', comment_views.comment_remove, name='comment_remove'),
]