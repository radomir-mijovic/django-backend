from django.urls import path
from .views import (
    ProductsFeedbackListView,
    GetUpdateDeleteFeedbackView,
    CreateCommentView,
    CreateReplyView
)

app_name = 'product_feedback'

urlpatterns = [
    path('products-feedback-list/', ProductsFeedbackListView.as_view(), name='products_feedback_list'),
    path('product-update-delete/<int:pk>/', GetUpdateDeleteFeedbackView.as_view(), name='product_update_delete'),

    path('create-comment/', CreateCommentView.as_view(), name='create_comment'),
    path('create-reply/', CreateReplyView.as_view(), name='create_reply'),
]
