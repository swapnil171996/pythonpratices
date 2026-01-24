import pytest

#if we add marker skip then  2 passed, 2 skipped,
'''test_feature_cases.py::testfd_addition PASSED                                                                                                          [ 25%] 
test_feature_cases.py::testfd_subtraction SKIPPED (unconditional skip)                                                                                 [ 50%] 
test_feature_cases.py::testfd_multiplication SKIPPED (featureis not avalible)                                                                          [ 75%] 
test_feature_cases.py::testfd_division PASSED  [100%] 

#if we add @pytest.mark.xfail

pytest.mark.xfail is used to mark a test that you expect to fail. 
Pytest will run it, but if it fails, the suite still passes. 
If it unexpectedly passes, pytest reports it as an XPASS (unexpected pass).

if test is pass then xpassed and if test case failed then xfailed
 2 skipped, 1 xfailed, 1 xpassed,
 
 - Xfail = “expected fail”.
- You use it when a test is known to fail due to:
- A bug not yet fixed.
- A feature not yet implemented.
- A dependency issue that isn’t resolved.
- It lets you keep the test in your suite without breaking your CI/CD pipeline.

'''

env="Prod"
@pytest.mark.smoke
@pytest.mark.xfail
def testfd_addition():
    a1=50
    b1=60
    c1=30
    assert a1+b1+c1==110
@pytest.mark.smoke
@pytest.mark.skip
def testfd_subtraction():
    a1=50
    b1=60
    c1=30
    assert a1-b1-c1==30
@pytest.mark.sanity
@pytest.mark.skipif(env=="Prod",reason="featureis not avalible ")
def testfd_multiplication():
    a1=50
    b1=60
    assert a1*b1
@pytest.mark.regression
@pytest.mark.xfail

def testfd_division():
    a1=20
    b1=4
    c1=30
    assert a1/b1==5

#to run test cases type cmd in terminal python -m pytest -v .\test_some_cases.py

'''
- python -m pytest
Runs the pytest module using Python. The -m flag tells Python to run a library module as a script. 
This ensures you’re using pytest installed in the same environment as your Python interpreter.
- -v (verbose mode)
Increases the level of detail in the test output. Instead of just showing dots (.) for passed tests, 
pytest will display the names of test functions and their results (PASSED, FAILED, SKIPPED, etc.).

- .\test_some_cases.py
Specifies the exact test file to run.
- .\ means “in the current directory” (PowerShell syntax).
- test_some_cases.py is the file containing your test functions.

✅ What happens when you run it
- Pytest will open test_some_cases.py.
- It will look for functions whose names start with test_ (e.g., def test_addition():).
- It will execute each test function.
- With -v, you’ll see output like:
============================= test session starts =============================
platform win32 -- Python 3.12.3, pytest-9.0.2
collected 3 items

test_some_cases.py::test_addition PASSED
test_some_cases.py::test_subtraction PASSED
test_some_cases.py::test_division FAILED



⚡ Pro Tips
- If you omit the filename:
python -m pytest -v
- Pytest will auto-discover all files named test_*.py or *_test.py in the folder.

- If you want to run a specific test function inside the file:
python -m pytest -v test_some_cases.py::test_addition
👉 So in short:
This command runs pytest in verbose mode on the file test_some_cases.py, showing detailed results for each test function inside it
'''

