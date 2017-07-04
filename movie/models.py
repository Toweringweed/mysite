from django.db import models

# Create your models here.
class Mclass(models.Model):
    m_class = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return self.m_class

class Marea(models.Model):
    m_area = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return self.m_area

class Myear(models.Model):
    m_year = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return self.m_year

class Mtag(models.Model):
    m_tag = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.m_tag

class Martist(models.Model):
    art_id = models.IntegerField(unique=True, default=-1)
    art_name = models.CharField(max_length=100)
    art_info = models.CharField(max_length=1000)
    art_intro = models.CharField(max_length=8000)
    art_award = models.CharField(max_length=2000)
    art_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.art_name

class Malist(models.Model):
    m_id = models.IntegerField()
    art_type = models.IntegerField()
    art_id = models.IntegerField()

class Mdetail(models.Model):
    m_id = models.IntegerField(unique=True, default=-1)
    m_name = models.CharField('电影名称', max_length=80)
    m_name2 = models.CharField(max_length=80, default="无")
    m_other_name = models.CharField(max_length=100, default='无')
    m_director = models.CharField(max_length=100, default='无')
    m_writer = models.CharField(max_length=100, default='无')
    m_actor = models.CharField(max_length=500, default='无')
    m_class = models.ForeignKey(Mclass)
    m_year = models.ForeignKey(Myear)
    m_tag = models.ManyToManyField(Mtag, related_name='m_id')
    m_area = models.ManyToManyField(Marea, related_name='m_id')
    m_lan = models.CharField(max_length=50, default='无')
    m_zimu = models.CharField(max_length=30, default='无')
    m_file_format = models.CharField(max_length=30, default='无')
    m_file_size = models.CharField(max_length=30, default='无')
    m_size = models.CharField(max_length=30, default='无')
    m_time = models.CharField(max_length=30, default='无')
    m_download = models.CharField(max_length=1000, default='无')
    m_douban_rating = models.FloatField(null=True, blank=True)
    m_douban_voters = models.IntegerField(null=True, blank=True)
    m_douban_url = models.CharField(max_length=100)
    m_imdb_rating = models.FloatField(null=True, blank=True)
    m_imdb_voters = models.IntegerField(null=True, blank=True)
    m_imdb_serial = models.CharField(max_length=100, default='无')
    m_imdb_url = models.CharField(max_length=100, default='无')
    m_poster = models.CharField(max_length=150, default='无')
    m_first_play = models.CharField(max_length=200, default='无')
    m_runtime = models.CharField(max_length=50, default='无')
    m_summary = models.CharField(max_length=3000, default='无')
    m_award = models.CharField(max_length=1500, default='无')
    m_comment_short = models.CharField(max_length=3000, default='无')
    m_comment_rating = models.CharField(max_length=200, default='无')
    m_season = models.IntegerField(null=True, blank=True)
    m_jishu = models.IntegerField(null=True, blank=True)
    m_time_ji = models.IntegerField(null=True, blank=True)
    m_update = models.DateTimeField(auto_now=True)
    m_update_douban = models.DateTimeField(null=True, blank=True)
    m_update_piaohua = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.m_name

