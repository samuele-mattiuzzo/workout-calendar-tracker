from django.db import models

# Create your models here.

STRENGTH = 0
CONDITIONING = 1
STRENGTH_EXTRA = 2
CONDITIONING_EXTRA = 3

WORKOUT_TYPES = [
    (STRENGTH, 'Strength'),
    (CONDITIONING, 'Conditioning'),
    (STRENGTH_EXTRA, 'Strength - extra'),
    (CONDITIONING_EXTRA, 'Conditioning - extra'),
]

class Session(models.Model):
    date = models.DateTimeField(
        'workout date', null=True, blank=True)
    
    
    program_name = models.CharField()
    program_phase = models.CharField()
    title = models.CharField()

    time_start_end = models.CharField()
    duration = models.CharField()
    total_sets = models.IntegerField()
    total_reps = models.IntegerField()
    average_weight = models.FloatField()
    total_weight = models.FloatField()

    description = models.TextField()

    def __str__(self):
        return '{} {} - {}'.format(
            self.program_name,
            self.program_phase,
            self.title
        )
