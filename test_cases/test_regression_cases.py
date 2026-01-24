import pytest

'''
python -m pytest -v -m smoke .\test_cases\

python -m pytest -v -m "smoke or regression" .\test_cases\
python -m pytest -v -m "smoke and regression" .\test_cases\
'''
@pytest.mark.smoke
def testfd_addition_reg():
    a1=50
    b1=60
    c1=30
    assert a1+b1+c1
@pytest.mark.smoke
@pytest.mark.regression

def testfd_subtraction_reg():
    a1=50
    b1=60
    c1=30
    assert a1-b1-c1==-20
@pytest.mark.sanity
def testfd_multiplication_reg():
    a1=50
    b1=60
    assert a1*b1==120
@pytest.mark.regression
def testfd_division_reg():
    a1=20
    b1=4
    c1=30
    assert a1/b1==5



