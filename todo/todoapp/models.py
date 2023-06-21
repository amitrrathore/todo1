from django.db import models

# Create your models here.

class todo(models.Model):
    content=models.CharField(max_length=300)
    completed=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.content

    # class Meta:
    #     ordering=['-date']