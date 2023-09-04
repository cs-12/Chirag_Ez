from django.db import models

# Create your models here.


from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    bio = models.TextField()

    def __str__(self):
        return self.user.username


        
class File(models.Model):
    TYPES = (
        ('pptx', 'PPTX'),
        ('docx', 'DOCX'),
        ('xlsx', 'XLSX'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    file_type = models.CharField(max_length=5, choices=TYPES)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.file.name}'