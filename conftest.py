import os

import pytest

STORAGE_STATE_PATH = "storage_state.json"


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """
    Load the saved NHS cookie consent state into every browser context, so the
    cookie banner does not interfere with the NHS tests.

    The state file is generated locally by setup_auth.py and is gitignored.
    If it is not present (for example in CI, where only the booking demo suite
    runs), contexts start without it.
    """
    if not os.path.exists(STORAGE_STATE_PATH):
        return browser_context_args

    return {
        **browser_context_args,
        "storage_state": STORAGE_STATE_PATH,
    }