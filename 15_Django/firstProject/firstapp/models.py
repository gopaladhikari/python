from django.db import models
from django.utils import timezone

# Create your models here.


class ChaiVariety(models.Model):
    chai_types = [
        ("ML", "Milk"),
        ("GR", "Ginger"),
        ("KL", "Kiwi"),
        ("EL", "Elaichi"),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=chai_types)
    description = models.TextField(default="")

    def __str__(self):
        return self.name
