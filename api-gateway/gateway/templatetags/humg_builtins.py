# -*- coding: utf-8 -*-
"""
Filter dùng chung cho mọi template (đăng ký trong TEMPLATES['OPTIONS']['builtins']).

Dữ liệu lấy từ các microservice qua API là JSON, nên ngày giờ về dạng chuỗi
("2026-11-18", "2026-11-18T11:23:14+07:00", "29/11/2026"). Filter `date`
mặc định của Django trả về chuỗi rỗng với giá trị kiểu str, làm các cột ngày
trên giao diện bị trống. Bản ở đây đọc được chuỗi ngày rồi chuyển cho filter
gốc của Django; với giá trị date/datetime thì hành vi không đổi.
"""
from datetime import date as _date, datetime as _datetime

from django import template
from django.template.defaultfilters import date as _django_date, time as _django_time
from django.utils import timezone
from django.utils.dateparse import parse_date, parse_datetime

register = template.Library()

_TEXT_FORMATS = ('%d/%m/%Y %H:%M:%S', '%d/%m/%Y %H:%M', '%d/%m/%Y', '%d-%m-%Y', '%Y/%m/%d')


def to_datetime(value):
    """Chuyển chuỗi ngày/giờ từ API thành date hoặc datetime (None nếu không đọc được)."""
    if isinstance(value, (_date, _datetime)):
        return value
    if not isinstance(value, str):
        return None
    text = value.strip()
    if not text:
        return None
    try:
        parsed = parse_datetime(text)
        if parsed is None:
            parsed = parse_date(text)
    except ValueError:
        parsed = None
    if parsed is None:
        for fmt in _TEXT_FORMATS:
            try:
                parsed = _datetime.strptime(text, fmt)
                if fmt in ('%d/%m/%Y', '%d-%m-%Y', '%Y/%m/%d'):
                    parsed = parsed.date()
                break
            except ValueError:
                continue
    if isinstance(parsed, _datetime) and timezone.is_aware(parsed):
        parsed = timezone.localtime(parsed)
    return parsed


@register.filter(expects_localtime=True, is_safe=False)
def date(value, arg=None):
    """Như filter `date` của Django nhưng nhận được cả chuỗi ngày từ API."""
    if isinstance(value, str):
        parsed = to_datetime(value)
        if parsed is None:
            return ''
        value = parsed
    return _django_date(value, arg)


@register.filter(expects_localtime=True, is_safe=False)
def time(value, arg=None):
    """Như filter `time` của Django nhưng nhận được cả chuỗi giờ từ API."""
    if isinstance(value, str):
        parsed = to_datetime(value)
        if not isinstance(parsed, _datetime):
            return ''
        value = parsed
    return _django_time(value, arg)


@register.filter
def to_date(value):
    """Ép chuỗi ngày từ API thành đối tượng date/datetime (dùng với so sánh, timesince...)."""
    parsed = to_datetime(value)
    return parsed if parsed is not None else value
