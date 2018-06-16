from rest_framework import serializers
from .models import Task, Instance, History

class TaskSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Task
        fields = ('id', 'title', 'status', 'created_date', 'owner_id', 'instance_id', 'population', 'generations', 'proc', 'wpz')
        
class InstanceSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Instance
        fields = ('id', 'title', 'graph', 'cityCount', 'owner_id')
        
class HistorySerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = History
        fields = ('id', 'title', 'graph', 'cityCount', 'owner_id', 'time', 'population', 'generations', 'proc', 'wpz')