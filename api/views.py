from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

from .models import Task
# Create your views here.

# This is a decorator provided by the DRF. It specifies that the following function (apiOverview) is a view that can handle HTTP GET requests
@api_view(['GET'])
def apiOverview(request):
	# api_urls is a dictionary containing various API endpoints and their corresponding paths.
	# The function returns a JSON response (Response(api_urls)) containing the API endpoints.
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

	return Response(api_urls)


# Function retrieves all tasks from the database, orders them by their IDs in descending order, serializes the tasks using the TaskSerializer, and returns the serialized data as a JSON response.
@api_view(['GET'])
def taskList(request):
	tasks = Task.objects.all().order_by('-id')
	serializer = TaskSerializer(tasks, many=True)
	return Response(serializer.data)


# function gets the specific task (using pk) -> serializes it and return it as a JSON response
@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Task.objects.get(id=pk)
	serializer = TaskSerializer(tasks, many=False)
	return Response(serializer.data)


# now this view handles POST requests.
@api_view(['POST'])
def taskCreate(request):
	# this is very similar to model forms where we use request.POST to get the data submitted by the user
	# The TaskSerializer is responsible for validating and converting this data into a format that can be saved to the database.
	serializer = TaskSerializer(data=request.data)

	#  If the data is valid, this line saves the serialized data to the database using the save method of the serializer. This assumes that the serializer is associated with a Django model (Task), and it will create a new task instance in the database.
	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request, pk):
	task = Task.objects.get(id=pk)
	# instance of this task is passed because we want the same task to update with the new data
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully deleted!')



