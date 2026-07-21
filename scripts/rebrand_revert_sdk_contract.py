from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "node_modules", "__pycache__"}
SKIP_FILES = {"poetry.lock", "uv.lock", "package-lock.json"}

# SDK discriminated union only accepts agent_kind tags: openhands, llm, acp.
SDK_CONTRACT_REPLACEMENTS = [
    ("agent_kind='openhands'", "agent_kind='openhands'"),
    ("agent_kind: str = 'openhands'", "agent_kind: str = 'openhands'"),  # no-op guard
    ("'agent_kind': 'openhands'", "'agent_kind': 'openhands'"),
    ("== 'omniagent'", "== 'openhands'"),  # too broad - need careful
]

# Targeted SDK contract restores (avoid broad == replacement)
TARGETED = [
    ("agent_kind='openhands'", "agent_kind='openhands'"),
    ("agent_kind: str = 'openhands'", "agent_kind: str = 'openhands'"),
    ("'agent_kind': 'openhands'", "'agent_kind': 'openhands'"),
    ("resolved.agent_kind == 'openhands'", "resolved.agent_kind == 'openhands'"),
    (
        "response.agent_settings.agent_kind == 'openhands'",
        "response.agent_settings.agent_kind == 'openhands'",
    ),
    ("['openhands', 'acp']", "['openhands', 'acp']"),
    ('useState<"openhands" | "acp">("openhands")', 'useState<"openhands" | "acp">("openhands")'),
    ('setAgentType("openhands")', 'setAgentType("openhands")'),
    ('key: "openhands"', 'key: "openhands"'),
    ('as "openhands" | "acp"', 'as "openhands" | "acp"'),
    ('agent_kind: "openhands"', 'agent_kind: "openhands"'),
    ('activeProvider === "openhands"', 'activeProvider === "openhands"'),
    ('selectedProvider === "openhands"', 'selectedProvider === "openhands"'),
    ('variant: "openhands"', 'variant: "openhands"'),
    ('case "openhands"', 'case "openhands"'),
    ('kind: "openhands"', 'kind: "openhands"'),
    ('agentKind === "openhands"', 'agentKind === "openhands"'),
    ('| "openhands"', '| "openhands"'),
    ('"openhands",', '"openhands",'),
    ('provider: "omniagent"', 'provider: "omniagent"'),  # skip
    ("  openhands:", "  openhands:"),  # map-provider - revert key only in ts files
    ('"openhands" | "acp"', '"openhands" | "acp"'),
    ('AgentKind = "openhands" | "acp"', 'AgentKind = "openhands" | "acp"'),
]

for path in ROOT.rglob("*"):
    if not path.is_file() or path.name in SKIP_FILES:
        continue
    if any(p in SKIP_DIRS for p in path.parts):
        continue
    if path.suffix not in {".py", ".ts", ".tsx", ".json"}:
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        continue
    original = text
    for old, new in TARGETED:
        if old == ('provider: "omniagent"', 'provider: "omniagent"'):
            continue
        text = text.replace(old, new)
    if text != original:
        path.write_text(text, encoding="utf-8")
        print(path.relative_to(ROOT))
