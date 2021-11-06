import time
from logging import Logger
from typing import Protocol


class AddServiceProtocol(Protocol):
    """
    Represents functionality of adding two numbers.
    """

    def add(self, a: int, b: int) -> int:
        ...


class AddService:
    """
    Implements AddServiceProtocol.
    """

    def add(self, a: int, b: int) -> int:
        return a + b


class LoggingAddService:
    """
    Implements AddServiceProtocol. Wraps AddService and adds basic logging.
    """

    def __init__(self, service: AddServiceProtocol, logger: Logger) -> None:
        self._inner = service
        self._logger = logger

    def add(self, a: int, b: int) -> int:
        result = self._inner.add(a, b)
        self._logger.debug("[add] adding %s and %s gives %s", a, b, result)
        return result


class TimingAddService:
    """
    Implements AddServiceProtocol. Wraps AddService and adds timing of method calls.
    """

    def __init__(self, service: AddServiceProtocol, logger: Logger) -> None:
        self._inner = service
        self._logger = logger

    def add(self, a: int, b: int) -> int:
        start = time.perf_counter()
        result = self._inner.add(a, b)
        end = time.perf_counter()
        elapsed = end - start
        self._logger.debug(f"[add] took {elapsed:0.8f} seconds")
        return result
