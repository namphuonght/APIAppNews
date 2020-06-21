from django.db import models

# Create your models here.


class Loai(models.Model):
    loai = models.CharField(max_length=255, verbose_name='Loại')

    def __str__(self):
        return self.loai

    class Meta:
        verbose_name = 'Loại'
        verbose_name_plural = 'Loại'


class TinTuc(models.Model):
    tieu_de = models.CharField(max_length=255, verbose_name='Tiêu đề')
    url_img = models.CharField(max_length=255, verbose_name='Link ảnh')
    mo_ta = models.CharField(max_length=1000, verbose_name='Mô tả')
    phan_loai = models.ForeignKey(Loai, on_delete=models.CASCADE, verbose_name='Loại')
    gio_dang = models.TimeField

    def __int__(self):
        return self.id

    class Meta:
        verbose_name = 'Tiêu đề'
        verbose_name_plural = 'Tiêu đề'


class NoiDung(models.Model):
    tieude = models.ForeignKey(TinTuc, on_delete=models.CASCADE, verbose_name='ID tiêu đề')
    noi_dung = models.CharField(max_length=10000, verbose_name='nội dung')
    url_imgNoiDung = models.CharField(max_length=255, verbose_name="Ảnh nội dung")
    url_video = models.CharField(max_length=355, verbose_name='Link video', null=True)

    class Meta:
        verbose_name = 'Nội dung'
        verbose_name_plural = 'Nội dung'


class Video(models.Model):
    tieu_de = models.CharField(max_length=255, verbose_name='Tiêu đề')
    url_video = models.CharField(max_length=355, verbose_name='Link video')

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Video'


class TaiKhoan(models.Model):
    tai_khoan = models.CharField(primary_key=True, max_length=255, verbose_name='Tài khoản')
    mat_khau = models.CharField(max_length=255, verbose_name='Mật khẩu')

    class Meta:
        verbose_name = 'Tài khoản'
        verbose_name_plural = 'Tài khoản'


class Comment(models.Model):
    noi_dung = models.ForeignKey(NoiDung, verbose_name='Thuộc nội dung', on_delete=models.CASCADE)
    taikhoan = models.ForeignKey(TaiKhoan, verbose_name='Của tài khoản', on_delete=models.CASCADE)
    comment = models.CharField(max_length=355, verbose_name='Bình luận')

    class Meta:
        verbose_name = 'Bình luận'
        verbose_name_plural = 'Bình luận'









