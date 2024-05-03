from rest_framework import serializers
from .models import (Files, Task) 

class FileSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Files
        fields = '__all__'
        
        # validate file extension
    def validate_file(self, value):
       
        allowed_extensions = ['ppt', 'pdf', 'doc', 'docx', 'png', 'jpeg', 'jpg', 'msg', 'xlsx', 'xls', 'txt']
        if value.name.split('.')[-1] not in allowed_extensions:
            raise serializers.ValidationError("Only .ppt, .pdf, .doc, .docx, .png, .jpeg, .jpg, .msg, .xlsx, .xls, .txt files are allowed.")
        return value
    
    def create(self, validated_data):
        file_type=validated_data['file_upload'].name.split('.')[-1]
        return file_type

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
