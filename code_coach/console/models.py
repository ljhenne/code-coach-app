from django.contrib.postgres.fields import ArrayField
from django.db import models


class Problem(models.Model):
    name = models.TextField()
    url = models.TextField()
    topics = ArrayField(models.TextField())


class ProblemAttempt(models.Model):
    CODING = 'CODING'
    FINISHED = 'FINISHED'
    PAUSED = 'PAUSED'
    STATE_CHOICES = [
        (CODING, 'Coding'),
        (FINISHED, 'Finished'),
        (PAUSED, 'Paused')
    ]
    closed_ts = models.DateTimeField()
    elapsed_time = models.DurationField()
    problem_id = models.ForeignKey(Problem, on_delete=models.CASCADE)
    state = models.CharField(max_length=8, choices=STATE_CHOICES, default=CODING)
    user_id = models.UUIDField()
