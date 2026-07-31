import pytest


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """
    Load the saved consent state into every browser context, so the cookie
    banner does not interfere with tests.

    The banner itself is tested separately in tests that explicitly use a
    clean context without this storage state.
    """
    return {
        **browser_context_args,
        "storage_state": "storage_state.json",
    }