from django.db import models

# Create your models here.
class Roundinfo(models.Model):
    id = models.IntegerField(primary_key=True)
    firstnum = models.IntegerField(db_column='firstNum')  # Field name made lowercase.
    secondnum = models.IntegerField(db_column='secondNum')  # Field name made lowercase.
    thirdnum = models.IntegerField(db_column='thirdNum')  # Field name made lowercase.
    fourthnum = models.IntegerField(db_column='fourthNum')  # Field name made lowercase.
    fifthnum = models.IntegerField(db_column='fifthNum')  # Field name made lowercase.
    sixthnum = models.IntegerField(db_column='sixthNum')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roundInfo'