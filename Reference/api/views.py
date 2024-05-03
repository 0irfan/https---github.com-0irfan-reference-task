from rest_framework import generics
from .permissions import IsAdmin
from .models import (Files, Task, Notes)
from .serializers import (FileSerializer,TaskSerializer, Noteserializer)
from  rest_framework.generics import (ListCreateAPIView , RetrieveUpdateDestroyAPIView)
from uuid import uuid4

# Create your views here.
class Files(ListCreateAPIView): #GEt All FIles  , CReate File /Upload File
    queryset = Files.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAdmin]

    

class File(RetrieveUpdateDestroyAPIView): #Get Single File  , Update FIle ,Delete file
    queryset=Files.objects.all()
    serializer_class=FileSerializer

    
            
class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAdmin]



class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class NotesCreate(generics.ListCreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer


class NotesCreate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer


    
