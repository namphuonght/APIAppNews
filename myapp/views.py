from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TinTuc, NoiDung, Video, TaiKhoan, Comment
from .serializers import GetTinTuc, GetVideo, GetComment, GetNoidung, GetTaiKhoan, GetIDTieuDe
from rest_framework.decorators import api_view
from django.http import Http404


# Create your views here.


class GetTinTucview(APIView):

    def get(self, request):
        list_tintuc = TinTuc.objects.all()
        tintuc = GetTinTuc(list_tintuc, many=True)
        return Response(data=tintuc.data, status=status.HTTP_200_OK)


class GetNoiDungview(APIView):
    def get(self, request):
        list_tintuc = NoiDung.objects.all()
        tintuc = GetNoidung(list_tintuc, many=True)
        return Response(data=tintuc.data, status=status.HTTP_200_OK)

    def post(self, request):
        pk = GetIDTieuDe(data=request.data)
        if pk.is_valid():
            id = pk.data['id']
            list_noidung = NoiDung.objects.filter(tieude=id)
            noidung = GetNoidung(list_noidung, many=True)
            return Response(data=noidung.data, status=status.HTTP_200_OK)
        return Response('bad request', status=status.HTTP_400_BAD_REQUEST)


class GetVideoview(APIView):

    def get(self, request):
        list_video = Video.objects.all()
        video = GetVideo(list_video, many=True)
        return Response(data=video.data, status=status.HTTP_200_OK)


class GetTaiKhoanview(APIView):

    def get(self, request):
        list_taikhoan = TaiKhoan.objects.all()
        taikhoan = GetTaiKhoan(list_taikhoan, many=True)
        return Response(data=taikhoan.data, status=status.HTTP_200_OK)


class GetCommentview(APIView):

    def get(self, request):
        list_comment = Comment.objects.all()
        comment = GetComment(list_comment, many=True)
        return Response(data=comment.data, status=status.HTTP_200_OK)
