# DEPRECATED: This module is deprecated and will be removed in a future release.
# Please use omniagent.app_server.middleware instead.
#
# For backward compatibility, this module re-exports from omniagent.app_server.middleware.

from omniagent.app_server.middleware import (
    CacheControlMiddleware,
    InMemoryRateLimiter,
    LocalhostCORSMiddleware,
    RateLimitMiddleware,
)

__all__ = [
    'LocalhostCORSMiddleware',
    'CacheControlMiddleware',
    'InMemoryRateLimiter',
    'RateLimitMiddleware',
]
