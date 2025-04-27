from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True, null=True)
    cover = models.ImageField(upload_to='posts/covers/', blank=True, null=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='posts')
    views_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  f"Model<{self.title}>"
    

