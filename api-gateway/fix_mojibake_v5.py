import pathlib, re

# Bắt mọi dải ký tự có thể là mojibake (mọi CP1252 non-ASCII)
MOJI_PATTERN = re.compile(
    r'[\u00A0-\u00FF\u0080-\u009F\u0152\u0153\u0160\u0161'
    r'\u0178\u017D\u017E\u0192\u02C6\u02DC\u2013\u2014'
    r'\u2018\u2019\u201A\u201B\u201C\u201D\u201E'
    r'\u2020\u2021\u2022\u2026\u2030\u2039\u203A\u20AC\u2122]+'
)

def reverse_run(s):
    out = bytearray()
    for c in s:
        try:
            out.extend(c.encode('cp1252'))
        except UnicodeEncodeError:
            if ord(c) <= 0xff:
                out.extend(bytes([ord(c)]))
            else:
                return None
    try:
        return bytes(out).decode('utf-8')
    except UnicodeDecodeError:
        return None

def looks_like_vietnamese(s):
    # Phải chứa ít nhất 1 ký tự Latin Extended-A (dấu tiếng Việt đúng)
    return any('\u0100' <= c <= '\u017f' for c in s)

fixed_list = []
skip_list = []

for f in pathlib.Path('templates').rglob('*.html'):
    if 'admin_bak' in str(f):
        continue

    raw = f.read_bytes()
    if raw.startswith(b'\xef\xbb\xbf'):
        raw = raw[3:]

    try:
        text = raw.decode('utf-8')
    except UnicodeDecodeError as e:
        skip_list.append((f, f'utf8 decode: {e}'))
        continue

    state = {'changed': False}

    def replacer(m):
        original = m.group(0)
        fixed = reverse_run(original)
        if fixed is None or fixed == original:
            return original
        if not looks_like_vietnamese(fixed):
            return original
        state['changed'] = True
        return fixed

    new_text = MOJI_PATTERN.sub(replacer, text)

    if state['changed']:
        f.write_bytes(new_text.encode('utf-8'))
        fixed_list.append(f)

print(f"✅ Đã fix: {len(fixed_list)} file")
for f in fixed_list:
    print(f"  [FIXED] {f}")

if skip_list:
    print(f"\n❌ Bỏ qua: {len(skip_list)} file")
    for f, e in skip_list:
        print(f"  [SKIP] {f}: {e}")
