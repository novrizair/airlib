from django.db import models

class Items(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()

    nama = models.CharField(max_length = 255)
    kelas = models.CharField(max_length = 255)
    aplikasi = models.CharField(max_length = 255)