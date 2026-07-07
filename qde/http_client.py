"""Thin HTTP GET wrapper. Mirrors include/qde/http_client.hpp + src/http_client.cpp.

Nothing finance-specific here on purpose -- same reasoning as the C++ version:
if you swap Yahoo for another vendor later, this file doesn't change.
"""
from dataclasses import dataclass
import requests


@dataclass
class HttpResponse:
    status_code: int = 0
    body: str = ""

    def ok(self) -> bool:
        return 200 <= self.status_code < 300


class HttpClient:
    """Equivalent of qde::HttpClient. requests already handles connection
    pooling / redirects / TLS verification, so this wrapper is thinner than
    its C++ counterpart -- but kept as its own file for the same reason:
    isolate networking from parsing logic.
    """

    def __init__(self, user_agent: str = "Mozilla/5.0 (X11; Linux x86_64) qde-data-engine/1.0"):
        self.user_agent = user_agent

    def get(self, url: str, headers: dict | None = None, timeout: int = 20) -> HttpResponse:
        req_headers = {"User-Agent": self.user_agent}
        if headers:
            req_headers.update(headers)
        try:
            resp = requests.get(url, headers=req_headers, timeout=timeout)
        except requests.RequestException as e:
            raise RuntimeError(f"request failed: {e}") from e
        return HttpResponse(status_code=resp.status_code, body=resp.text)
