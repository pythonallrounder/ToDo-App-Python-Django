from django.db import models

# Create your models here.

class todo(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_length=200)
    author_name = models.CharField(max_length=50)
    
    

    def __str__(self):
        return 'Author : {0} Book_Name : {1} Added_Date : {2}'.format(self.author_name,self.text,self.added_date)

