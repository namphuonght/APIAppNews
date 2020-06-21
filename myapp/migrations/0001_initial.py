# Generated by Django 3.0.7 on 2020-06-08 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loai', models.CharField(max_length=255, verbose_name='Loại')),
            ],
            options={
                'verbose_name': 'Loại',
                'verbose_name_plural': 'Loại',
            },
        ),
        migrations.CreateModel(
            name='TaiKhoan',
            fields=[
                ('tai_khoan', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='Tài khoản')),
                ('mat_khau', models.CharField(max_length=255, verbose_name='Mật khẩu')),
            ],
            options={
                'verbose_name': 'Tài khoản',
                'verbose_name_plural': 'Tài khoản',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tieu_de', models.CharField(max_length=255, verbose_name='Tiêu đề')),
                ('url_video', models.CharField(max_length=355, verbose_name='Link video')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Video',
            },
        ),
        migrations.CreateModel(
            name='TinTuc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tieu_de', models.CharField(max_length=255, verbose_name='Tiêu đề')),
                ('url_img', models.CharField(max_length=255, verbose_name='Link ảnh')),
                ('mo_ta', models.CharField(max_length=1000, verbose_name='Mô tả')),
                ('phan_loai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Loai', verbose_name='Loại')),
            ],
            options={
                'verbose_name': 'Tiêu đề',
                'verbose_name_plural': 'Tiêu đề',
            },
        ),
        migrations.CreateModel(
            name='NoiDung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noi_dung', models.CharField(max_length=10000, verbose_name='nội dung')),
                ('url_imgNoiDung', models.CharField(max_length=255, verbose_name='Ảnh nội dung')),
                ('url_video', models.CharField(max_length=355, null=True, verbose_name='Link video')),
                ('tieude', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.TinTuc', verbose_name='Tiêu đề')),
            ],
            options={
                'verbose_name': 'Nội dung',
                'verbose_name_plural': 'Nội dung',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=355, verbose_name='Bình luận')),
                ('noi_dung', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.NoiDung', verbose_name='Thuộc nội dung')),
                ('taikhoan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.TaiKhoan', verbose_name='Của tài khoản')),
            ],
            options={
                'verbose_name': 'Bình luận',
                'verbose_name_plural': 'Bình luận',
            },
        ),
    ]
