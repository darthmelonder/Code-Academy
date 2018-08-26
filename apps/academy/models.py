from django.db import models
# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length = 26)
    password = models.CharField(max_length = 20)
    name = models.CharField(max_length = 26)
    mysingle = models.CharField(max_length = 20)
    number_of_problems = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Problems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField (max_length=100)

class Problems_List (models.Model):
    problem_name = models.CharField (max_length=100)
    problem_description = models.TextField()
    problem_input = models.FileField()
    problems_output = models.FileField(upload_to='documents')
    uploaded_at = models.DateTimeField(auto_now_add=True)
  #  uploaded_by = models.CharField (max_length=26)
    def __str__ (self):
        return self.problem_name

