from django.db import models

# Create your models here.

# each class represent table of database
# each class varibae represent table colomn

# crateing Topic Table
class Topic(models.Model):
    #crating colomnn
    topic_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.topic_name
        
    
#creatiing Web_page table
class Web_Page(models.Model):
    #creating colmon
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()
    def __str__(self):
        return self.name
    
        

#crating Access_record table
class Access_Record(models.Model):
    #creating colmon
    name=models.ForeignKey(Web_Page,on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)
    def __str__(self):
        return self.date
        
    