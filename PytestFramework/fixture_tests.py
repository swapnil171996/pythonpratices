import pytest

"""

fixture: fixture is the function which will work as pre-requisite of 
any test case/test file or test packages.

---fixture scopes:---
function scope:function level will apply of all the test cases and execute setup and 
                tear down for the each test case.
module scope:-
package scope
session scope
class scope

To check fixture executed correctly
 python -m pytest -v -s .\fixture_tests.
 
 @pytest.fixture(scope='function',autouse="True")
 if we mention autouse="True then it will apply fixtures for all functions.
 no need to mention for each function ex.def testfd_addition(fun_setup):
 
ex.
fixture_tests.py::testfd_addition :-function
--Function code execution started--:-start setup
FAILED                             :-execution
 --function execution is done---   :tear down



"""
@pytest.fixture(scope='function')
def fun_setup():
    print("\n--Function code execution started--")
    yield #tear down section of fixture
    print("\n --function execution is done---")

@pytest.fixture(scope='module',autouse=True)
def module_setup():
    print("\n--module code execution started--")
    yield #tear down section of fixture
    print("\n --module execution is done---")

@pytest.fixture(scope='package',autouse=True")
def package_setup():
    print("\n--package code execution started--")
    yield #tear down section of fixture
    print("\n --package execution is done---")

@pytest.fixture(scope='session',autouse="True")
def session_setup():
    print("\n--session code execution started--")
    yield #tear down section of fixture
    print("\n --session execution is done---")
@pytest.mark.smoke
def testfd_addition(fun_setup):
    a1=50
    b1=60
    c1=30
    assert a1+b1+c1==110
@pytest.mark.smoke
def testfd_subtraction(fun_setup):
    a1=50
    b1=60
    c1=30
    assert a1-b1-c1==30
@pytest.mark.sanity
def testfd_multiplication(fun_setup):
    a1=50
    b1=60
    assert a1*b1
@pytest.mark.regression
def testfd_division(fun_setup):
    a1=20
    b1=4
    c1=30
    assert a1/b1==5



