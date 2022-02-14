from django.db import models

# Create your models here.


class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    from_hospital_id = models.CharField('from_hospital_id', max_length=255, null=True)
    target_hospital_id = models.CharField('target_hospital_id', max_length=255, null=True)
    # from_hospital_id = models.ForeignKey('Hospitals', related_name='hospital_id', on_delete=models.RESTRICT, \
    # name='hospital_from')
    # target_hospital_id = models.ForeignKey('Hospitals', related_name='hospital_id', on_delete=models.RESTRICT, \
    # name='hospital_target')
    created_time = models.DateTimeField('created_time', null=True)
    title = models.CharField('title', max_length=255, null=True)
    description = models.TextField('description', null=True)
    status = models.IntegerField('status', null=True, default=0)
    type = models.CharField('type', max_length=255, null=True)

    class Meta:
        db_table = 'Notifications'
        indexes = [
            models.Index(fields=['from_hospital_id'], name='hospital_from'),
            models.Index(fields=['target_hospital_id'], name='hospital_target')
        ]
