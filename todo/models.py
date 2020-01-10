from django.db import models

# Create your models here.
# represents each todo item in our database
# use this class to interact with the data in our database
class TodoItem(models.Model):
    # attribute = content, can add more attributes for each item later
    # content represents the content of each item which is text
    content = models.TextField()
