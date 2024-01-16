# Serializers in Django are used to convert complex data types (such as Django models) to Python data types that can be easily rendered into JSON.

from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		# The serializer will be used to convert instances of the Task model to and from JSON.
		model = Task
		fields ='__all__'