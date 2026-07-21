#!/usr/bin/env python3
"""One-shot rebrand: OpenHands / all-hands / openhands.dev -> OmniAgent / ismailubts/OmniAgent."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SKIP_DIRS = {
    ".git",
    ".venv",
    "node_modules",
    "build",
    "dist",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    "coverage",
}

SKIP_FILES = {
    "poetry.lock",
    "uv.lock",
    "package-lock.json",
    "rebrand_omniagent.py",
}

BINARY_SUFFIXES = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".ico",
    ".woff",
    ".woff2",
    ".ttf",
    ".eot",
    ".zip",
    ".gz",
    ".pdf",
    ".pyc",
    ".whl",
}

# Lines matching these patterns are left unchanged (external SDK/runtime deps).
SKIP_LINE_PATTERNS = [
    re.compile(r"^\s*from openhands\."),
    re.compile(r"^\s*import openhands\b"),
    re.compile(r"^\s*from openhands import"),
    re.compile(r"openhands-sdk"),
    re.compile(r"openhands-agent-server"),
    re.compile(r"openhands-tools"),
    re.compile(r"ghcr\.io/openhands/"),
    re.compile(r"@openhands/agent-canvas"),
    re.compile(r"VERIFIED_OPENHANDS_MODELS as"),
    re.compile(r"OpenHandsModel\b"),
    re.compile(r"OpenHandsUUID\b"),
    re.compile(r"OpenHandsAgentSettings\b"),
    re.compile(r"f'openhands/\{"),
    re.compile(r'f"openhands/\{'),
    re.compile(r"'openhands/\{"),
    re.compile(r'"openhands/\{'),
    re.compile(r"openhands/\{m\}"),
    re.compile(r"DEFAULT_OMNIAGENT_MODEL = 'openhands/"),
    re.compile(r"^#.*openhands"),
]

REPO = "https://github.com/ismailubts/OmniAgent"
REPO_BLOB = f"{REPO}/blob/main"

REPLACEMENTS: list[tuple[str, str]] = [
    # URLs — old docs & product sites -> this repo
    ("https://docs.all-hands.dev/usage/getting-started", f"{REPO}#quickstart"),
    ("https://docs.all-hands.dev/usage/prompting/microagents-repo", f"{REPO_BLOB}/skills/README.md"),
    ("https://docs.all-hands.dev/usage/prompting/repository#setup-script", f"{REPO_BLOB}/Development.md"),
    ("https://docs.all-hands.dev/usage/prompting/prompting-best-practices", f"{REPO_BLOB}/Development.md"),
    ("https://docs.all-hands.dev/usage/how-to/headless-mode", f"{REPO_BLOB}/Development.md"),
    ("https://docs.all-hands.dev/usage/how-to/cli-mode", f"{REPO_BLOB}/Development.md"),
    (
        "https://docs.all-hands.dev/usage/cloud/github-installation#working-on-github-issues-and-pull-requests-using-openhands",
        f"{REPO_BLOB}/README.md",
    ),
    ("https://docs.all-hands.dev/usage/cloud/github-installation", f"{REPO_BLOB}/README.md"),
    ("https://docs.all-hands.dev/usage/cloud/openhands-cloud", f"{REPO_BLOB}/README.md"),
    ("https://docs.all-hands.dev/usage/cloud/cloud-api", f"{REPO_BLOB}/Development.md"),
    ("https://docs.all-hands.dev/usage/cloud/slack-installation", f"{REPO_BLOB}/README.md"),
    ("https://docs.all-hands.dev/usage/prompting/microagents-overview", f"{REPO_BLOB}/skills/README.md"),
    ("https://docs.all-hands.dev/usage/prompting/microagents-org", f"{REPO_BLOB}/skills/README.md"),
    ("https://docs.all-hands.dev/api-reference/health-check", f"{REPO_BLOB}/Development.md"),
    ("https://docs.all-hands.dev", REPO),
    ("https://docs.openhands.dev", REPO),
    ("https://docs.omniagent.dev/usage/local-setup#getting-an-api-key", f"{REPO}#quickstart"),
    ("https://docs.omniagent.dev/usage/llms/openhands-llms", f"{REPO_BLOB}/Development.md"),
    ("https://docs.omniagent.dev/omniagent/", f"{REPO_BLOB}/"),
    ("https://docs.omniagent.dev", REPO),
    ("https://www.all-hands.dev/blog", REPO),
    ("https://www.all-hands.dev/tos", f"{REPO_BLOB}/LICENSE"),
    ("https://www.all-hands.dev/privacy", f"{REPO_BLOB}/LICENSE"),
    ("https://www.all-hands.dev", REPO),
    ("https://app.all-hands.dev/settings/api-keys", f"{REPO}#quickstart"),
    ("https://app.all-hands.dev", REPO),
    ("https://openhands.dev/enterprise/", REPO),
    ("https://openhands.dev/enterprise", REPO),
    ("https://openhands.dev", REPO),
    # Repo references
    ("OpenHands/OpenHands", "ismailubts/OmniAgent"),
    ("github.com/OpenHands/OpenHands", "github.com/ismailubts/OmniAgent"),
    ("github.com/openhands/openhands", "github.com/ismailubts/OmniAgent"),
    # Product names
    ("Agent Canvas", "OmniAgent"),
    ("agent-canvas", "omniagent"),
    ("Open Hands", "OmniAgent"),
    ("OpenHands", "OmniAgent"),
    # Integration handles & config names
    ("@openhands", "@omniagent"),
    ("openhands-config", "omniagent-config"),
    ("openhands-app", "omniagent-app"),
    ("openhands:cross-app-reload", "omniagent:cross-app-reload"),
    ("openhands_login_method", "omniagent_login_method"),
    ("openhands_enterprise_form_saas", "omniagent_enterprise_form_saas"),
    ("openhands_enterprise_form_self_hosted", "omniagent_enterprise_form_self_hosted"),
    ("openhands_selected_org", "omniagent_selected_org"),
    ("openhands@all-hands.dev", "omniagent@users.noreply.github.com"),
    ("openhands@659478cb008c", "omniagent@workspace"),
    ("OHE Admin Config", "OmniAgent Admin Config"),
    # i18n / API keys
    ("BRANDING$OPENHANDS", "BRANDING$OMNIAGENT"),
    ("SETTINGS$AGENT_TYPE_OPENHANDS", "SETTINGS$AGENT_TYPE_OMNIAGENT"),
    ("openhands-account-help", "omniagent-account-help"),
    ("openhands_version", "omniagent_version"),
    ("openhandsVersion", "omniagentVersion"),
    # File / import paths
    ("open-hands-axios", "omniagent-axios"),
    ("open-hands.types", "omniagent-api.types"),
    ("openHands", "omniAgentApi"),
    # Agent kind / provider identifiers (project-owned)
    ('agent_kind: "openhands"', 'agent_kind: "openhands"'),
    ("agent_kind: 'openhands'", "agent_kind: 'omniagent'"),
    ('agent_kind = "openhands"', 'agent_kind = "omniagent"'),
    ("agent_kind = 'openhands'", "agent_kind = 'omniagent'"),
    ('"openhands" | "acp"', '"openhands" | "acp"'),
    ('"openhands" | \'acp\'', '"omniagent" | \'acp\''),
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
    ('git_user_name: "openhands"', 'git_user_name: "OmniAgent"'),
    ('provider: "openhands"', 'provider: "omniagent"'),
    ("  openhands:", "  openhands:"),
    # Table / store names in our code
    ("openhands_prs", "omniagent_prs"),
    ("OpenhandsPr", "OmniagentPr"),
    # Remaining lowercase brand in prose (after specific patterns)
    ("openhands.dev", "github.com/ismailubts/OmniAgent"),
    ("all-hands.dev", "github.com/ismailubts/OmniAgent"),
]

# Apply longer replacements first where order matters
REPLACEMENTS.sort(key=lambda x: len(x[0]), reverse=True)


def should_skip_line(line: str) -> bool:
    return any(p.search(line) for p in SKIP_LINE_PATTERNS)


def process_file(path: Path) -> bool:
    if path.name in SKIP_FILES:
        return False
    if path.suffix.lower() in BINARY_SUFFIXES:
        return False
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return False

    original = text
    lines = text.splitlines(keepends=True)
    out_lines: list[str] = []
    for line in lines:
        if should_skip_line(line):
            out_lines.append(line)
            continue
        new_line = line
        for old, new in REPLACEMENTS:
            new_line = new_line.replace(old, new)
        out_lines.append(new_line)

    new_text = "".join(out_lines)
    if new_text != original:
        path.write_text(new_text, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed = 0
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if process_file(path):
            changed += 1
            print(f"updated: {path.relative_to(ROOT)}")
    print(f"\nDone. {changed} files updated.")


if __name__ == "__main__":
    main()
