# OmniAgent Enterprise Server

> [!NOTE]
> Copyright (c) Abdul Ismail. All rights reserved. See the root [LICENSE](../LICENSE).

> [!WARNING]
> This is a work in progress and may contain bugs, incomplete features, or breaking changes.

This directory contains the enterprise server for OmniAgent.

**Author:** [Abdul Ismail](https://github.com/ismailubts)  
**Repository:** https://github.com/ismailubts/OmniAgent

## Extension of OmniAgent

The code in `/enterprise` builds on top of OmniAgent, extending its functionality. The enterprise code is entangled with OmniAgent in two ways:

- Enterprise stacks on top of OmniAgent. For example, the middleware in enterprise is stacked right on top of the middlewares in OmniAgent.

- Enterprise overrides the implementation in OmniAgent (only one is present at a time). For example, the server config SaasServerConfig overrides [`ServerConfig`](https://github.com/ismailubts/OmniAgent/blob/main/omniagent/server/config/server_config.py#L8) in OmniAgent.

Key areas that change on `SAAS` are:

- Authentication
- User settings

## Development

See [enterprise_local/README.md](./enterprise_local/README.md) for local development setup.
