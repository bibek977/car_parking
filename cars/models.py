from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from datetime import date
from django.utils import timezone
from django.db.models.signals import post_delete,post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

def today_date():
    return date.today()

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    created_at = models.DateField(auto_now=True)
    update_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class Cars(BaseModel):
    brand = models.CharField(_("brand_name"),max_length=200)
    color = models.CharField(_("color"),max_length=200)
    liscense_no = models.CharField(_("liscense_no"),max_length=50,unique=True)
    owner = models.CharField(_("Car_owner_name"),max_length=100,default="Annonymous")
    status = models.BooleanField(_("car_park_status"),default=False)

    def __str__(self):
        return self.liscense_no
    
    class Meta:
        verbose_name = _("Car")
        verbose_name_plural = _("Cars")


class Space(BaseModel):
    space_box = models.CharField(_("space_identity"),max_length=10,unique=True)
    status = models.BooleanField(_("space status"),default=False)

    def __str__(self):
        return self.space_box

    class Meta:
        verbose_name = _("Space")
        verbose_name_plural = _("Space")

class ParkSlot(BaseModel):
    car = models.ForeignKey(Cars,on_delete=models.CASCADE)
    space = models.ForeignKey(Space,on_delete=models.CASCADE)
    date = models.DateField(default=today_date)
    status = models.BooleanField(default=True)
    out = models.DateField(blank=True,null=True)

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name_plural = _("Park Slot")
        verbose_name_plural = _("Parking Slots")

@receiver(post_save, sender=ParkSlot)
def parked_in(sender,instance,created,**kwargs):
    if created:
        s=Space.objects.get(space_box=instance.space)
        s.status = True
        s.save()

        c = Cars.objects.get(liscense_no=instance.car)
        c.status = True
        c.save()