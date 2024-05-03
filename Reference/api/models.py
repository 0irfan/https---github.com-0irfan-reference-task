from django.db import models
from utils.reference_utils.model_choices import SECTION_CHOICES


class Task(models.Model):
    id = models.UUIDField(primary_key= True,editable= False)
    company = models.ForeignKey("model",on_delete= models.CASCADE)
    job = models.ForeignKey("model",on_delete= models.CASCADE)
    applicant = models.ForeignKey("model", on_delete= models.CASCADE)
    title = models.CharField(max_length= 255, null= False)
    start_date = models.DateField(null= False)
    end_date = models.DateField(null= False)
    
    class Meta:
        db_table = "reference_task" 

# Create your models here.
class Files(models.Model):
    refernce_id = models.ForeignKey(Task,on_delete= models.CASCADE)
    date_added = models.DateTimeField(auto_now_add= True)
    name = models.URLField()
    file_name = models.FileField(max_length = 255 , null = True)
    file_type  = models.CharField(max_length = 255 , null = True)
    file_mode = models.CharField(max_length = 25, choices = SECTION_CHOICES ,null = True)
    file_size = models.CharField(max_length = 255, null = True)
    file_upload = models.FileField(upload_to = 'files/')

    class Meta:
        db_table = "reference_files"


