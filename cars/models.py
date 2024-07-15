from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _

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
