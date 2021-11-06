from django.urls import path
from .views import TodosView, TodoUpdateDeleteView, DeleteCompletedView

app_name = 'todo_fm'

urlpatterns = [
    path('todos/', TodosView.as_view(), name='todos'),
    path('update-delete/<int:pk>/', TodoUpdateDeleteView.as_view(), name='update_delete'),
    path('delete-completed-todos/', DeleteCompletedView.as_view(), name='delete_completed')
]