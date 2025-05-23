from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    CATEGORY_CHOICES = [
        ('Design', 'Design'),
        ('Coding', 'Coding'),
        ('Content', 'Content'),
        ('Presentation', 'Presentation'),
        ('Media', 'Media'),
        ('Translation', 'Translation'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    estimated_time = models.CharField(max_length=100)
    reward = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_jobs')
    accepted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='accepted_jobs')
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.posted_by.username}'
