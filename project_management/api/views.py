from rest_framework import viewsets, generics, permissions
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer, UserRegisterSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

# Project Views
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

# Task Views
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Task.objects.all()
        project = self.request.query_params.get('project')
        status = self.request.query_params.get('status')
        due_date = self.request.query_params.get('due_date')

        if project:
            queryset = queryset.filter(project_id=project)
        if status:
            queryset = queryset.filter(status=status)
        if due_date:
            queryset = queryset.filter(deadline__lte=due_date)

        return queryset

# User Registration View
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Add default role "Developer" to new users
            developer_group, created = Group.objects.get_or_create(name='Developer')
            user.groups.add(developer_group)
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from .permissions import IsAdminOrPMCanEdit

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsAdminOrPMCanEdit]  # <--- added

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsAdminOrPMCanEdit]  # <--- added
