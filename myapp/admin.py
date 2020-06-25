from django.contrib import admin
from .models import TinTuc, NoiDung, Video, TaiKhoan, Comment, Loai

# Register your models here.


class TinTucAdmin(admin.ModelAdmin):
    list_display = ('id_tintuc', 'tieu_de', 'url_img', 'phan_loai')


class NoiDungAdmin(admin.ModelAdmin):
    list_display = ('tieude', 'mo_bai', 'url_imgNoiDung', 'ket_bai')


class VideoAdmin(admin.ModelAdmin):
    list_display = ('tieu_de', 'url_video')


class TaiKhoanAdmin(admin.ModelAdmin):
    list_display = ('tai_khoan', 'mat_khau')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('noi_dung', 'taikhoan', 'comment')


class LoaiAdmin(admin.ModelAdmin):
    list_display = ('loai', )


admin.site.register(TinTuc, TinTucAdmin)
admin.site.register(NoiDung, NoiDungAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(TaiKhoan, TaiKhoanAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Loai, LoaiAdmin)


admin.site.site_header = 'Nam Phương'