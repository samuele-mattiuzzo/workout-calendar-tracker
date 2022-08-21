from django.db import models

STRENGTH = '0'
CONDITIONING = '1'
ACTIVE_REST = '2'
WORKOUT_TYPES = [
    (STRENGTH, 'Strength'),
    (CONDITIONING, 'Conditioning'),
    (ACTIVE_REST, 'Active rest')
]

class Session(models.Model):
    date = models.DateTimeField(
        'workout date', null=True, blank=True)
    program_name = models.CharField(max_length=200)
    program_phase = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    workout_type = models.CharField(max_length=200, choices=WORKOUT_TYPES, default=ACTIVE_REST)
    time_start_end = models.CharField(max_length=200, null=True, blank=True)
    duration = models.CharField(max_length=200, null=True, blank=True)
    total_sets = models.IntegerField(null=True, blank=True)
    total_reps = models.IntegerField(null=True, blank=True)
    average_weight = models.FloatField(null=True, blank=True)
    total_weight = models.FloatField(null=True, blank=True)

    description = models.TextField(null=True, blank=True)
    class Meta:
        ordering = ['-date',]

    def __str__(self):
        return '{} {} - {} {}'.format(
            self.program_name,
            self.program_phase,
            self.name,
            self.date.strftime('%d-%m-%Y')
        )
