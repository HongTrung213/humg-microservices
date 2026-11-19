from django.db import migrations, models


def doi_tin_chi_sang_tdnn(apps, schema_editor):
    DotThi = apps.get_model('exams', 'DotThi')
    DotThi.objects.filter(loai='TIN_CHI').update(loai='TDNN')


def tdnn_ve_tin_chi(apps, schema_editor):
    DotThi = apps.get_model('exams', 'DotThi')
    DotThi.objects.filter(loai='TDNN').update(loai='TIN_CHI')


class Migration(migrations.Migration):
    """Mỗi đợt thi là một môn: CĐR CNTT, CĐR Ngoại ngữ, Trình độ ngoại ngữ (TĐNN)."""

    dependencies = [
        ('exams', '0002_remove_lichsuthi_dat_remove_lichsuthi_diem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dotthi',
            name='loai',
            field=models.CharField(choices=[('CDR_TH', 'Chuẩn đầu ra Công nghệ thông tin'), ('CDR_NN', 'Chuẩn đầu ra Ngoại ngữ'), ('TDNN', 'Trình độ ngoại ngữ')], max_length=20),
        ),
        migrations.AlterField(
            model_name='lichsuthi',
            name='mon_thi',
            field=models.CharField(choices=[('TA_DAU_VAO', 'Trình độ ngoại ngữ'), ('CDR_NGOAI_NGU', 'Chuẩn đầu ra Ngoại ngữ'), ('CDR_TIN_HOC', 'Chuẩn đầu ra Công nghệ thông tin')], default='CDR_NGOAI_NGU', max_length=20),
        ),
        migrations.RunPython(doi_tin_chi_sang_tdnn, tdnn_ve_tin_chi),
    ]
