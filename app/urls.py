
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from tarefas.views import DownloadTaskFile, TaskListView, CreateTaskView, TaskDetailView, TaskUpdateView, TaskDeleteView
from accounts.views import register_view, login_view, logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
      path('tasks/', TaskListView.as_view(), name="tasks_list" ),
       path('task/<int:task_id>/download/', DownloadTaskFile.as_view(), name='download_task_file'),
       path('new_task', CreateTaskView.as_view(), name="new_task"),
       path('register', register_view, name="register"),
       path('login', login_view, name="login"),
       path('logout', logout_view, name="logout"),
       path('task/<int:pk>', TaskDetailView.as_view(), name="task_detail"),
       path('task/<int:pk>/delete', TaskDeleteView.as_view(), name="task_delete"),
       path('task/<int:pk>/update', TaskUpdateView.as_view(), name="task_update"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
