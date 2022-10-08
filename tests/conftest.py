"""Fixtures for static data used by tests."""
import sys

import pytest


@pytest.fixture
def capture_stdout(monkeypatch):
    """Define fixture to capture stdout."""
    buffer = {"stdout": "", "write_calls": 0}

    def fake_write(s):
        buffer["stdout"] += s
        buffer["write_calls"] += 1

    monkeypatch.setattr(sys.stdout, "write", fake_write)
    return buffer
