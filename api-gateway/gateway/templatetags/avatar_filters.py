# -*- coding: utf-8 -*-
"""Template tags cho avatar dong."""
import hashlib
from urllib.parse import quote

from django import template

register = template.Library()

_AVATAR_COLORS = [
    '#C8102E', '#1e40af', '#0891b2', '#7c3aed', '#db2777',
    '#ea580c', '#059669', '#0284c7', '#9333ea', '#ca8a04',
]


def _initials(name):
    if not name:
        return '?'
    parts = str(name).strip().split()
    if not parts:
        return '?'
    if len(parts) == 1:
        return parts[0][:2].upper()
    return (parts[0][0] + parts[-1][0]).upper()


def _color(seed):
    if not seed:
        return _AVATAR_COLORS[0]
    h = int(hashlib.md5(str(seed).encode('utf-8')).hexdigest(), 16)
    return _AVATAR_COLORS[h % len(_AVATAR_COLORS)]


def make_avatar_url(anh_dai_dien, ho_ten, ma_sv='', size=200):
    if anh_dai_dien:
        return anh_dai_dien
    initials = _initials(ho_ten)
    color = _color(ma_sv or ho_ten)
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" '
        f'viewBox="0 0 {size} {size}">'
        f'<rect width="100%" height="100%" fill="{color}"/>'
        f'<text x="50%" y="50%" dy=".1em" fill="#ffffff" '
        f'font-family="Arial,Helvetica,sans-serif" '
        f'font-size="{size // 2.5:.0f}" font-weight="bold" '
        f'text-anchor="middle" dominant-baseline="middle">{initials}</text>'
        f'</svg>'
    )
    return f'data:image/svg+xml;charset=utf-8,{quote(svg)}'


@register.simple_tag
def avatar_url(anh_dai_dien=None, ho_ten='', ma_sv='', size=200):
    return make_avatar_url(anh_dai_dien, ho_ten, ma_sv, size)