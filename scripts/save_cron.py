#!/usr/bin/env python3
import sqlite3, os, datetime

DB = '/home/hermes/.hermes/state.db'
OUT = '/opt/data/hermes-conversations/sessions'

sessions = [
    ('cron_705be3976f88_20260830_200028', 'session_20260830_200028_cron_705.md'),
    ('cron_6665b97efca7_20260830_070023', 'session_20260830_070023_cron_666.md'),
    ('cron_1bc5e10e1893_20260830_000059', 'session_20260830_000059_cron_1bc.md'),
]

con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row
cur = con.cursor()

def to_jst(ts):
    return datetime.datetime.fromtimestamp(ts, datetime.timezone(datetime.timedelta(hours=9))).strftime('%Y-%m-%d %H:%M:%S')

for sid, fname in sessions:
    cur.execute("SELECT id, model, started_at, ended_at, message_count FROM sessions WHERE id=?", (sid,))
    s = cur.fetchone()
    cur.execute("SELECT role, content, timestamp FROM messages WHERE session_id=? AND role IN ('user','assistant') ORDER BY timestamp, id", (sid,))
    rows = cur.fetchall()

    lines = []
    lines.append(f"# Session: {sid}")
    lines.append("")
    lines.append(f"- 開始: {to_jst(s['started_at']) if s else '?'}")
    lines.append(f"- 終了: {to_jst(s['ended_at']) if s else '?'}")
    lines.append(f"- メッセージ数(user/assistant): {len(rows)}")
    if s and s['model']:
        lines.append(f"- Model: {s['model']}")
    lines.append("")
    lines.append("---")
    lines.append("")
    for m in rows:
        role = 'マスター' if m['role'] == 'user' else 'アシスタント'
        ts = to_jst(m['timestamp'])
        content = (m['content'] or '').strip()
        lines.append(f"### {role} ({ts})")
        lines.append("")
        lines.append(content)
        lines.append("")

    path = os.path.join(OUT, fname)
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f"WROTE {path} ({len(rows)} msgs)")