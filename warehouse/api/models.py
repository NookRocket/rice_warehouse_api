# from django.db import models
from datetime import datetime
from djongo import models
from utils import import_csv
from django.urls import reverse

class Seed(models.Model):
    rep_date = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
    year_week = models.IntegerField(null=True)
    varity = models.CharField(max_length=100)
    rdcsd = models.CharField(max_length=100)
    stock2sale = models.CharField(max_length=100)
    season = models.IntegerField(null=True)
    crop_year = models.CharField(max_length=100)

    def save(self, *arg, **kwargs):
        self.pk = self.increase_pk()
        if not self.rep_date:
            self.rep_date = datetime.now().strftime("%Y%m%d")
        super().save(*arg, **kwargs)
    
    def increase_pk(self):
        pk_list = [s.pk for s in Seed.objects.all()]
        return 1 if not pk_list else pk_list[-1]+1

    def get_absolute_url(self):
        return reverse('api:detail', kwargs={'pk':self.pk})

def init_seed_data():
    data_list = import_csv.csv_to_dict_list("././static/data/data.csv")
    for data in data_list:
        model = Seed(**data)
        model.save()
