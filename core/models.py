from django.db import models


class User(models.Model):
    userid = models.BigAutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    usernick = models.CharField(db_column='UserNick', max_length=80, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    userlink = models.CharField(db_column='UserLink', max_length=2047, blank=True, null=True)  # Field name made lowercase.
    userfrom = models.CharField(db_column='UserFrom', max_length=100, blank=True, null=True)  # Field name made lowercase.
    userscor = models.DecimalField(db_column='UserScor', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.username
    
    class Meta:
        managed = False
        db_table = 'USER'