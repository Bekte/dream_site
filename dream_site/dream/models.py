from django.db import models

from django.db import models


class Courses(models.Model):
    # amount_student = models.IntegerField()
    course_title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    cost = models.IntegerField(blank=True)
    image = models.ImageField(upload_to='articles/')
    # cat = models.ForeignKey('Teachers', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.course_title


class Teachers(models.Model):
    name = models.CharField(max_length=100)
    direction = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='articles/')
    is_published = models.BooleanField(default=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    image = models.ImageField(upload_to='articles/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='articles/')
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class TransferTest(models.Model):
    categories = models.CharField(max_length=255)

    def __str__(self):
        return self.categories


class Categories(models.Model):
    title = models.CharField(max_length=255)
    parent_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.title


class Tasks(models.Model):
    text = models.CharField(max_length=255)
    category_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.text


class Questions(models.Model):
    text = models.CharField(max_length=255)
    category_id = models.IntegerField(blank=True)
    task_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.text


class TaskInputOptions(models.Model):
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(blank=True)
    task_input_id = models.IntegerField(blank=True)
    task_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.text


class TaskInputs(models.Model):
    position = models.IntegerField(blank=True)
    task_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.position
