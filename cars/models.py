from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from datetime import date
from django.utils import timezone

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    created_at = models.DateField(auto_now=True)
    update_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class Cars(BaseModel):
    brand = models.CharField(_("brand_name"),max_length=200)
    color = models.CharField(_("color"),max_length=200)
    liscense_no = models.CharField(_("liscense_no"),max_length=50)

    def __str__(self):
        return self.liscense_no
    
    class Meta:
        verbose_name_plural = "Car"
        verbose_name_plural = "Cars"


class Space(BaseModel):
    space_box = models.CharField(_("space_identity"),max_length=10)
    status = models.BooleanField(_("space status"),default=False)
    def __str__(self):
        return self.space_box


class ParkSlot(BaseModel):
    car = models.ForeignKey(Cars,on_delete=models.CASCADE)
    space = models.ForeignKey(Space,on_delete=models.CASCADE)
    date = models.DateField(default=date.today())

    def __str__(self):
        return str(self.date)