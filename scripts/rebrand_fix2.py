from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "node_modules", "__pycache__"}
SKIP_FILES = {"poetry.lock", "uv.lock", "package-lock.json", "rebrand_omniagent.py", "rebrand_fix2.py"}

REPLACEMENTS = [
    ("OmniAgentAgentSettings", "OpenHandsAgentSettings"),
    ("'app': 'openhands'", "'app': 'omniagent'"),
    ("agent_kind='openhands'", "agent_kind='openhands'"),
    ("agent_kind: str = 'openhands'", "agent_kind: str = 'openhands'"),
    ("'agent_kind': 'openhands'", "'agent_kind': 'openhands'"),
    ("app:openhands", "app:omniagent"),
    ("['openhands', 'acp']", "['openhands', 'acp']"),
    ("resolved.agent_kind == 'openhands'", "resolved.agent_kind == 'openhands'"),
    ("response.agent_settings.agent_kind == 'openhands'", "response.agent_settings.agent_kind == 'openhands'"),
    ("'agent_kind': 'openhands'", "'agent_kind': 'openhands'"),
]

for path in ROOT.rglob("*"):
    if not path.is_file() or path.name in SKIP_FILES:
        continue
    if any(p in SKIP_DIRS for p in path.parts):
        continue
    if path.suffix in {".png", ".jpg", ".pyc", ".whl"}:
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        continue
    original = text
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    if text != original:
        path.write_text(text, encoding="utf-8")
        print(path.relative_to(ROOT))
