import pathlib

MOJIBAKE_MARKERS = ['chá»§', 'ÄÄƒng', 'Quáº£n', 'Há»§y',
                    'Khoa há»c', 'Sinh viÃªn', 'NgÃ nh',
                    'Chá»©ng chá»‰', 'ThÃ´ng bÃ¡o']

def char_to_reversed_bytes(c):
    """Encode 1 ký tự về byte gốc (reverse mojibake)."""
    try:
        return c.encode('cp1252')
    except UnicodeEncodeError:
        if ord(c) <= 0xff:
            # Control chars U+0080-U+009F (0x90, 0x8d, 0x81, 0x9d...) → latin-1
            return bytes([ord(c)])
        # Ký tự Unicode thật (không thể reverse) → giữ nguyên dạng utf-8
        return c.encode('utf-8')

fixed_list = []
skip_list = []
bom_stripped = []

for f in pathlib.Path('templates').rglob('*.html'):
    if 'admin_bak' in str(f):
        continue

    raw = f.read_bytes()
    had_bom = raw.startswith(b'\xef\xbb\xbf')
    if had_bom:
        raw = raw[3:]

    try:
        text = raw.decode('utf-8')
    except UnicodeDecodeError as e:
        skip_list.append((f, f'utf8 decode: {e}'))
        continue

    if not any(m in text for m in MOJIBAKE_MARKERS):
        if had_bom:
            f.write_bytes(raw)
            bom_stripped.append(f)
        continue

    out = bytearray()
    for c in text:
        out.extend(char_to_reversed_bytes(c))

    try:
        fixed = bytes(out).decode('utf-8')
    except UnicodeDecodeError as e:
        skip_list.append((f, f'reverse decode: {e}'))
        continue

    f.write_bytes(fixed.encode('utf-8'))
    fixed_list.append(f)

print(f"✅ Đã fix: {len(fixed_list)} file")
for f in fixed_list:
    print(f"  [FIXED] {f}")

if bom_stripped:
    print(f"\n🧹 Strip BOM: {len(bom_stripped)} file")

if skip_list:
    print(f"\n❌ Bỏ qua: {len(skip_list)} file")
    for f, e in skip_list:
        print(f"  [SKIP] {f}: {e}")
