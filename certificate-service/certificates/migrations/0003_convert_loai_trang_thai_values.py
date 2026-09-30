from django.db import migrations


def convert_loai(apps, schema_editor):
    DanhMucChungChi = apps.get_model('certificates', 'DanhMucChungChi')
    # NN -> NGOAI_NGU
    DanhMucChungChi.objects.filter(loai='NN').update(loai='NGOAI_NGU')
    # TH -> TIN_HOC
    DanhMucChungChi.objects.filter(loai='TH').update(loai='TIN_HOC')


def convert_trang_thai(apps, schema_editor):
    ChungChi = apps.get_model('certificates', 'ChungChi')
    # ACTIVE -> DAT (giả định ACTIVE = chứng chỉ hợp lệ)
    ChungChi.objects.filter(trang_thai='ACTIVE').update(trang_thai='DAT')
    # INACTIVE / các trạng thái cũ khác -> HET_HAN
    ChungChi.objects.filter(trang_thai__in=['INACTIVE', 'EXPIRED']).update(trang_thai='HET_HAN')


def reverse_convert(apps, schema_editor):
    DanhMucChungChi = apps.get_model('certificates', 'DanhMucChungChi')
    DanhMucChungChi.objects.filter(loai='NGOAI_NGU').update(loai='NN')
    DanhMucChungChi.objects.filter(loai='TIN_HOC').update(loai='TH')

    ChungChi = apps.get_model('certificates', 'ChungChi')
    ChungChi.objects.filter(trang_thai='DAT').update(trang_thai='ACTIVE')


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0002_alter_chungchi_options_alter_chungchi_danh_muc_and_more'),
    ]

    operations = [
        migrations.RunPython(convert_loai, reverse_convert),
        migrations.RunPython(convert_trang_thai, reverse_convert),
    ]