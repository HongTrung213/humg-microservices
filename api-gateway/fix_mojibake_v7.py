import pathlib, re

MOJI_PATTERN = re.compile(
    r'[\u00A0-\u00FF\u0080-\u009F'
    r'\u0152\u0153\u0160\u0161\u0178\u017D\u017E\u0192'
    r'\u02C6\u02DC\u2013\u2014\u2018\u2019\u201A\u201B'
    r'\u201C\u201D\u201E\u2020\u2021\u2022\u2026\u2030'
    r'\u2039\u203A\u20AC\u2122]+'
)

def reverse_run_best(run):
    """Reverse mojibake. Trả về (decoded, consumed) hoặc (None, 0)."""
    byte_chunks = []
    for c in run:
        try:
            cb = c.encode('cp1252')
        except UnicodeEncodeError:
            if ord(c) <= 0xff:
                cb = bytes([ord(c)])
            else:
                break
        byte_chunks.append(cb)
    # Thử decode toàn bộ, rồi rút ngắn dần
    for n in range(len(byte_chunks), 0, -1):
        candidate = b''.join(byte_chunks[:n])
        try:
            return candidate.decode('utf-8'), n
        except UnicodeDecodeError:
            continue
    return None, 0

fixed_list = []
bom_list = []

for f in pathlib.Path('templates').rglob('*.html'):
    if 'admin_bak' in str(f):
        continue

    raw = f.read_bytes()
    had_bom = raw.startswith(b'\xef\xbb\xbf')
    if had_bom:
        raw = raw[3:]

    try:
        text = raw.decode('utf-8')
    except UnicodeDecodeError:
        continue

    changed = {'v': False}

    def replacer(m):
        run = m.group(0)
        decoded, consumed = reverse_run_best(run)
        if decoded is None:
            return run
        if decoded == run[:consumed]:
            return run
        changed['v'] = True
        return decoded + run[consumed:]

    new_text = MOJI_PATTERN.sub(replacer, text)

    if changed['v'] or had_bom:
        f.write_bytes(new_text.encode('utf-8'))
        if changed['v']:
            fixed_list.append(f)
        if had_bom:
            bom_list.append(f)

print(f"✅ Đã fix mojibake: {len(fixed_list)} file")
for f in fixed_list:
    print(f"  [FIXED] {f}")
if bom_list:
    print(f"\n🧹 Strip BOM: {len(bom_list)} file")
    for f in bom_list:
        print(f"  [BOM] {f}")
