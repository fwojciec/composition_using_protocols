import logging
import sys

from typer import Typer

from service import AddService, AddServiceProtocol, LoggingAddService, TimingAddService


app = Typer(name="add service")


def std_out_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter("[%(name)s] [%(levelname)s] %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


@app.command()
def add(a: int, b: int, debug: bool = False, timing: bool = False) -> None:
    service: AddServiceProtocol = AddService()
    if debug:
        service = LoggingAddService(service=service, logger=std_out_logger("logging"))
    if timing:
        service = TimingAddService(service=service, logger=std_out_logger("timing"))
    print(service.add(a, b))


if __name__ == "__main__":
    app()
