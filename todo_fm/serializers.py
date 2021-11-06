from rest_framework import serializers
from todo_fm.models import Todos


class TodosSerializer(serializers.ModelSerializer):
    completed = serializers.BooleanField(required=True)

    class Meta:
        model = Todos
        fields = '__all__'
