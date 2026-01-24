import pytest
from users_input import *
@pytest.mark.parametrize("username,password",[("user1","Admin@123"),
                                                ("user2","Admin@123"),
                                                ("user3","Admin@1234"),
                                                ("user4","user@123"),
                                                ("user5","root@123"),
                                                ("user6","testuser@123")])
def test_login(username,password):
    print("username:",username)
    print("password",password)

@pytest.mark.parametrize("username,password",User_detail
                         )
def test_login_with_external_data(username,password):
    print("username:",username)
    print("password",password)


