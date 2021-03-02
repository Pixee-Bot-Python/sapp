from typing import Any, Optional

from .session import Session

class scoped_session(
    Session
):  # not true at runtime, methods are set dynamically and wrapped
    session_factory: Any = ...
    registry: Any = ...
    def __init__(self, session_factory, scopefunc: Optional[Any] = ...) -> None: ...
    def __call__(self, **kw): ...
    def remove(self): ...
    def configure(self, **kwargs): ...
    def query_property(self, query_cls: Optional[Any] = ...): ...

ScopedSession = scoped_session