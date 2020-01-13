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
    title = models.CharField('название статьи', max_length=30)
    text = models.TextField('текст статьи')
    pub_date = models.DateTimeField('дата публикации')
    img = models.ImageField(upload_to='static/img/', blank=True, null=True)

    def to_dict(self):
        json = {
            'id': self.id,
            'title': self.title,
            'text': self.text,
            'pub_date': self.pub_date,
        }
        try:
            url = self.img.url
        except ValueError:
            url = ''
        json['img_url'] = url
        return json

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('имя автора', max_length=50)
    text = models.CharField('текст комментария', max_length=200)

    def to_dict(self):
        json = {
            'article_id': self.article.id,
            'author': self.author_name,
            'text': self.text
        }
        return json

    def __str__(self):
        return self.author_name