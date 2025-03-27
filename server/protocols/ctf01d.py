import httpx
from server.models import FlagStatus, SubmitResult


TIMEOUT = 5


def submit_flags(flags, config):
    for item in flags:
        response = httpx.get(config["SYSTEM_URL"], params={"teamid": config["SYSTEM_TOKEN"], "flag": item.flag}, timeout=TIMEOUT)
        if response.status_code == httpx.codes.OK:
            yield SubmitResult(item.flag, FlagStatus.ACCEPTED, response.text)
        elif response.status_code == httpx.codes.BAD_REQUEST:
            yield SubmitResult(item.flag, FlagStatus.QUEUED, response.text)
        elif response.status_code == httpx.codes.FORBIDDEN:
            yield SubmitResult(item.flag, FlagStatus.REJECTED, response.text)
        else:
            yield SubmitResult(item.flag, FlagStatus.QUEUED, response.text)

