from django.db import models
from posts.models import aparteman,vilae

class CommentAparteman(models.Model):
    Aparteman = models.ForeignKey(aparteman,on_delete=models.CASCADE,related_name='comments')
    Full_name = models.CharField(max_length=250)
    Email_address = models.EmailField(max_length=254)
    message = models.TextField(unique_for_date=True)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.Aparteman} از {self.Full_name}"


    class Meta:
        ordering = ('created',)

class CommentVilla(models.Model):
    Villae = models.ForeignKey(vilae,on_delete=models.CASCADE,related_name='commentsVillae')
    Full_name = models.CharField(max_length=250)
    Email_address = models.EmailField(max_length=254)
    message = models.TextField(unique_for_date=True)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.Villae} از {self.Full_name}"