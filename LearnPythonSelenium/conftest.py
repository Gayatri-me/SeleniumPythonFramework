import pytest


@pytest.fixture(scope="class",autouse=True)
def tc_setup():
    print("tc_setup")
    print("Started execution")
    yield
    print("Completed execution")
    print("tear down")
