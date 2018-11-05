from django.db import models


class Todo(models.Model):
    CHOICES = (
        (1, '아주 중요'),
        (2, '중요'),
        (3, '보통'),
        (4, '별로 안 중요'),
    )
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField(blank=True, null=True, db_index=True)
    is_done = models.BooleanField(default=False)
    priority = models.IntegerField(default=3, choices=CHOICES, db_index=True)

    def __str__(self):
        return self.title

    def set_expiration(self, datetime):
        self.expiration = datetime
        self.save()

    def done(self):
        self.is_done = True
        self.save()

    def set_priority(self, priority):
        self.priority = priority
        self.save()

    def swap_content(self, todo):
        self.title = todo.title
        self.content = todo.content
        self.expiration = todo.expiration
        self.priority = todo.priority
        self.save()

    def priority_verbose(self):
        return dict(self.CHOICES)[self.priority]
