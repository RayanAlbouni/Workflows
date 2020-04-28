from django.db import models

# Create your models here.
class Workflow(models.Model):
    """
    A workflow consist of Auto generated ID, Name, Description, and 0 or more steps.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()


class Step(models.Model):
    """
    A step consist of Auto generated ID, Name, order, description and a foreign key to the workflow model.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    order = models.IntegerField()
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE, related_name='steps')

    class Meta:
        unique_together = ('workflow', 'order')
        ordering = ['order']

class Comment(models.Model):
    """
    A comment consist of Auto generated ID, Name, text and a foreign key to the workflow model.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    text = models.TextField()
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE)
