from django.db import models
from uservalidation.models import *
# Create your models here.


class Appointment(models.Model):
    pass
    wm = models.ForeignKey(WM, on_delete=models.CASCADE)
    hni = models.ForeignKey(HNI, on_delete=models.CASCADE)
    date = models.DateTimeField()
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.wm.wm_id.getFullName()+" -> "+self.hni.hni_id.getFullName()
