from django.db import models



class Tree(models.Model):

    '''
    Уникалния номер на всяко дърво се образува както следва:
    - идентификатора на имота в който е дървото +
    - пореден номер от 1 до 999 за този имот
    '''
    tree_uid = models.CharField(max_length=48, unique=True, help_text='')

    tree_sp_bg = models.CharField(max_length=128, help_text='')
    tree_sp_lat = models.CharField(max_length=128, help_text='')

    tree_height = models.DecimalField(decimal_places=8, max_digits=12)
    tree_altitude = models.DecimalField(decimal_places=8, max_digits=12)
    tree_latitude = models.DecimalField(decimal_places=8, max_digits=12)
    tree_longitude = models.DecimalField(decimal_places=8, max_digits=12)
    tree_diameter = models.DecimalField(decimal_places=8, max_digits=12)

    is_decorative = models.BooleanField(default=False)
    is_invasive = models.BooleanField(default=False)
    is_healthy = models.BooleanField(default=True)

    def __str__(self):
        return '{}::{}'.format(self.tree_uid, self.tree_sp_bg)


