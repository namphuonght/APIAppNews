from rest_framework import serializers
from .models import TinTuc, NoiDung, Video, TaiKhoan, Comment


class GetTinTuc(serializers.ModelSerializer):

    class Meta:
        model = TinTuc
        fields = ('id_tintuc', 'tieu_de', 'url_img', 'mo_ta')


class GetNoidung(serializers.ModelSerializer):

    class Meta:
        model = NoiDung
        fields = ('tieude', 'mo_bai', 'url_imgNoiDung', 'ket_bai')


class GetIDTieuDe(serializers.Serializer):
    id = serializers.CharField(max_length=25)


class GetVideo(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ('tieu_de', 'url_video')


class GetTaiKhoan(serializers.ModelSerializer):

    class Meta:
        model = TaiKhoan
        fields = ('tai_khoan', 'mat_khau')


class GetComment(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('mat_khau', 'taikhoan', 'comment')


