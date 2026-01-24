import pytest

@pytest.mark.smoke
def testfd_addition_value():
    a1=50
    b1=60
    c1=30
    assert a1+b1+c1
@pytest.mark.smoke
def testfd_subtraction_value():
    a1=50
    b1=60
    c1=30
    assert a1-b1-c1==30
@pytest.mark.sanity
def testfd_multiplication_vaue():
    a1=50
    b1=60
    assert a1*b1
@pytest.mark.regression
def testfd_division_value():
    a1=20
    b1=4
    c1=30
    assert a1/b1==5

#