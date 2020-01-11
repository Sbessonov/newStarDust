from django.db import models

# Create your models here.
# первичный ключ создается автоматически id = models.AutoField()


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article_title = models.CharField('название статьи', max_length=30)
    author_text = models.TextField('текст статьи')
    pub_date = models.DateTimeField('дата публикации')
    img = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.article_title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('имя автора', max_length=50)
    comment_text = models.CharField('текст комментария', max_length=200)

    def __str__(self):
        return self.author_name