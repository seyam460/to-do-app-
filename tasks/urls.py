from django .urls import path 
from .views import task_list, add_task, edit_task, toggle_task, delete_task


urlpatterns = [
    path ("task_list/", task_list, name = "task_list"),
    path("add_task/", add_task, name="add_task"),
    path("edit_task/<int:id>/", edit_task, name="edit_task"),
    path("toggle_task/<int:id>/", toggle_task, name="toggle_task"),
    path("delete_task/<int:id>/", delete_task, name="delete_task"),
]
