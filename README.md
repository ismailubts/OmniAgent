<a name="readme-top"></a>
<div align="center">
  <h1>OmniAgent</h1>
  <p align="center">
    <strong>The self-hosted developer control center for coding agents and automations.</strong>
  </p>
  <p align="center">
    Run Claude Code, Codex, Gemini, or any ACP-compatible agent across local, remote, and cloud backends.
  </p>
</div>
<div align="center">
  <a href="https://github.com/ismailubts/OmniAgent"><img src="https://img.shields.io/badge/status-beta-blue?style=for-the-badge" alt="Project status beta"></a>
  <a href="https://github.com/ismailubts/OmniAgent/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/ismailubts/OmniAgent/ci.yml?branch=main&style=for-the-badge" alt="CI status"></a>
  <a href="https://github.com/ismailubts/OmniAgent/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT License"></a>
</div>
<div align="center">
  <a href="#quickstart">Quickstart</a> |
  <a href="#architecture">Architecture</a> |
  <a href="./Development.md">Development</a> |
  <a href="https://github.com/ismailubts/OmniAgent/issues">Issues</a>
</div>
<hr>

OmniAgent turns your coding agents into a self-hosted, always-on engineering team. It's a developer control center for starting conversations and automating everyday tasks — like generating reports that publish to Slack or automatically decomposing GitHub issues into tasks.

It runs locally on your machine by default, but can connect to multiple agent backends, e.g. running agents in Docker containers, on VMs, or within your company infrastructure.

OmniAgent includes a built-in coding agent out-of-the-box, but can use any third-party agent like Claude Code and Codex.

|    |    |
|---|---|
| **Self-host your way** | Run agents locally, in Docker, on VMs, or anywhere you can run an agent server backend |
| **Switch between backends** | Switch between local, remote, and cloud agents without losing focus |
| **Create automations** | Create automations and workflows that integrate with Slack, GitHub, Linear, and more |
| **Integrate with your tools** | Connect automations with third-party services like Slack, GitHub, Notion, and more |
| **Bring your own model** | Use with any LLM |
| **Use with any agent** | Claude Code, Codex, Gemini, or any ACP-compatible agent |

**Maintainer:** [Abdul Ismail](https://github.com/ismailubts)

If you have questions or feedback, please [open a GitHub issue](https://github.com/ismailubts/OmniAgent/issues).

## Quickstart

You can install OmniAgent to run agents on any machine: on your laptop, on a dedicated computer like a Mac Mini,
or on a server in the cloud.

### Option 1: Without a Sandbox

> [!WARNING]
> This runs the agent-server directly on the machine you're installing on — the agent will have full access to your filesystem!

**Prerequisites**: Node.js 22.12.x or later, Python 3.12, Poetry

```sh
git clone https://github.com/ismailubts/OmniAgent.git
cd OmniAgent
make build && make run
```

Then open the app in your browser and configure your LLM API key in **Settings**.

### Option 2: With a Docker Sandbox

**Prerequisites**:

- Docker: Docker Desktop on macOS/Windows, or Docker Engine/Docker Desktop on Linux.
- A host directory for `PROJECTS_PATH` containing the project folders you want the agent to access. Create it before starting the container.

**macOS / Linux:**

```sh
export PROJECTS_PATH="$HOME/projects"  # directory containing your project folders
mkdir -p "$PROJECTS_PATH" "$HOME/.omniagent"

docker run -it --rm \
  -p 8000:8000 \
  -v "$HOME/.omniagent:/home/omniagent/.omniagent" \
  -v "${PROJECTS_PATH}:/projects" \
  ghcr.io/openhands/agent-canvas:1
```

The agent will be able to access any project under `PROJECTS_PATH`.

### Option 3: From Source

> [!WARNING]
> This runs the agent-server directly on the machine you're installing on — the agent will have full access to your filesystem!

**Prerequisites**: Node.js 22.12.x or later, `npm`, `uv` (for running the agent server via `uvx`)

```sh
git clone https://github.com/ismailubts/OmniAgent.git
cd OmniAgent
npm install
npm run dev
```

---

Access the UI at [http://localhost:8000](http://localhost:8000). You can add additional backends directly from the UI.

## Architecture

OmniAgent is powered by the OmniAgent Agent Server, a REST API for running multiple agents on a single machine. Each Agent Server runs on a single host/port; OmniAgent can connect to multiple Agent Servers and easily flip between them.

You can run an Agent Server anywhere:

- Directly on your laptop (be careful!)
- On a dedicated machine like a Mac Mini
- On a virtual machine in the cloud

## More documentation

- [Architecture overview](#architecture)
- [Development guide](./Development.md)
- [Contributing guide](./CONTRIBUTING.md)
- [License](./LICENSE) — Copyright (c) 2026 Abdul Ismail
