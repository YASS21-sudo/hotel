from django.db import models

class RoomType(models.Model):
    name = models.CharField(max_length=250, unique=True, verbose_name="Nom")
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=250, verbose_name="Nom")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix")
    stock = models.PositiveIntegerField(default=0, verbose_name="Capacité")
    category = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True, related_name='rooms', verbose_name="Type de chambre")
    image = models.ImageField(null=True, upload_to='rooms/')

    def __str__(self):
        return self.name
