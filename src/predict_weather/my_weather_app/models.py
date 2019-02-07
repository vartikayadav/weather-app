from django.db import models

# Create your models here.
class City(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):#string rep of data kind of
        return self.name
    #we give our models meta data by meta class
    #modern meta data is anything that is not a field ,
    #such as ordering options (ordering), database table name (db_table),
    #or human-readable singular and plural names (verbose_name and verbose_name_plural).
    # None are required, and adding class Meta to a model is completely optional.
    class Meta:
        verbose_name_plural="cities"
