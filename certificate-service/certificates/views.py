from rest_framework import viewsets
from .models import DanhMucChungChi, ChungChi
from .serializers import DanhMucChungChiSerializer, ChungChiSerializer


class DanhMucChungChiViewSet(viewsets.ModelViewSet):
    queryset = DanhMucChungChi.objects.all()
    serializer_class = DanhMucChungChiSerializer


class ChungChiViewSet(viewsets.ModelViewSet):
    # ✅ Cần queryset cho DRF router
    queryset = ChungChi.objects.select_related('danh_muc').all()
    serializer_class = ChungChiSerializer

    def get_queryset(self):
        """Filter theo query params: sinh_vien_id, trang_thai, danh_muc."""
        qs = super().get_queryset()

        sinh_vien_id = self.request.query_params.get('sinh_vien_id')
        if sinh_vien_id:
            qs = qs.filter(sinh_vien_id=sinh_vien_id)

        trang_thai = self.request.query_params.get('trang_thai')
        if trang_thai:
            qs = qs.filter(trang_thai=trang_thai)

        danh_muc_id = self.request.query_params.get('danh_muc')
        if danh_muc_id:
            qs = qs.filter(danh_muc_id=danh_muc_id)

        return qs