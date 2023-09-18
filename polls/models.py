from django.db import models



from django.contrib.auth.models import User


class stakan(models.Model):
    name = models.CharField(max_length=220, default='')
    hajmi = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __str__(self) -> str:
        return self.name


class eshik(models.Model):
    nomi = models.CharField(max_length=201, default='')
    boyi = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __str__(self) -> str:
        return self.nomi