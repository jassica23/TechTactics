from django.db import models

class LFA(models.Model):
    problem = models.TextField()
    student_outcome = models.TextField(blank=True, null=True)
    activities = models.TextField(blank=True, null=True)
    stakeholders = models.TextField(blank=True, null=True)
    indicators = models.TextField(blank=True, null=True) 

    def __str__(self):
        return self.problem[:50]
