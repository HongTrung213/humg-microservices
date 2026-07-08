from django.db import models

class BaiViet(models.Model):
    tieu_de = models.CharField(max_length=200)
    noi_dung = models.TextField()
    slug = models.SlugField(unique=True)
    hinh_anh = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tieu_de

class Slider(models.Model):
    tieu_de = models.CharField(max_length=100)
    hinh_anh = models.URLField()
    duong_dan = models.CharField(max_length=200, blank=True)
    thu_tu = models.IntegerField(default=0)

    def __str__(self):
        return self.tieu_de

class QuickLink(models.Model):
    ten = models.CharField(max_length=100)
    duong_dan = models.CharField(max_length=200)
    thu_tu = models.IntegerField(default=0)

    def __str__(self):
        return self.ten