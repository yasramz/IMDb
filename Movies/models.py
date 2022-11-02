from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=50)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


class movies(models.Model):
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    release_date = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to='movies/avatars/', null=True, blank=True)
    genres = models.ManyToManyField(Genre)
    crew = models.ManyToManyField('crew')
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class crew(models.Model):
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    gender = models.IntegerField(null=True)
    birthday = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to='crew/avatars/', null=True, blank=True)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name, self.last_name

class role(models.Model):
    titel = models.CharField(max_length=50)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class moviescrew(models.Model):
    movie = models.ForeignKey(movies, on_delete=models.CASCADE)
    crew = models.ForeignKey(crew, on_delete=models.CASCADE)
    role = models.ForeignKey(role, on_delete=models.CASCADE)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
