import re
import pandas as pd
from django.db import transaction
from datetime import datetime

def normalize_key(text):
    text = str(text or '').lower().strip()
    text = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', text)
    text = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', text)
    text = re.sub(r'[ìíịỉĩ]', 'i', text)
    text = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', text)
    text = re.sub(r'[ùúụủũưừứựửữ]', 'u', text)
    text = re.sub(r'[ỳýỵỷỹ]', 'y', text)
    text = re.sub(r'đ', 'd', text)
    text = re.sub(r'[^a-z0-9]', '', text)
    return text

def clean_excel_val(val):
    if pd.isna(val):
        return ''
    if isinstance(val, float) and val.is_integer():
        return str(int(val))
    return str(val).strip()

def extract_mssv(value):
    raw = clean_excel_val(value)
    if raw.endswith('.0'):
        raw = raw[:-2]
    digits = re.sub(r'\D', '', raw)
    return digits if len(digits) >= 5 else ''

def to_float(val):
    if val is None or pd.isna(val):
        return None
    txt = str(val).strip().replace(',', '.')
    if not txt:
        return None
    try:
        return float(txt)
    except (TypeError, ValueError):
        return None

def read_excel_with_smart_header(excel_file, sheet_name=0):
    df_raw = pd.read_excel(excel_file, sheet_name=sheet_name, header=None)
    keywords = ['mssv', 'ma sinh vien', 'masv', 'mã sinh viên']
    header_idx = 0
    for i, row in df_raw.iterrows():
        row_text = ' '.join(str(v).lower() for v in row if pd.notna(v))
        if any(k in row_text for k in keywords):
            header_idx = i
            break
    df = df_raw.iloc[header_idx + 1:].copy()
    df.columns = [normalize_key(c) for c in df_raw.iloc[header_idx]]
    df = df.dropna(how='all')
    return df