import pytest

@pytest.fixture(scope="function",autouse=True)
def setup(request):
    print(f"\n conftest fixture initiated:{request.node.name}")
    yield
    print(f"\n conftest fixture completed:{request.node.name}")


@pytest.fixture(scope="module",autouse=True)
def module_setup():
    print("\n conftest module fixture initiated")
    yield
    print("\n conftest module fixture completed")


@pytest.fixture(scope="package",autouse=True)
def package_setup():
    print("\n conftest package fixture initiated")
    yield
    print("\n conftest package fixture completed")


@pytest.fixture(scope="session",autouse=True)
def session_setup():
    print("\n conftest session fixture initiated")
    yield
    print("\n conftest session fixture completed")

