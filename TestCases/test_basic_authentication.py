import requests
from requests.auth import  HTTPBasicAuth
def test_basic_auth():
    response = requests.get("https://api.github.com/user")
    print(response.text)
# C:\Users\hp\PycharmProjects\API_Student_Management_System\TestCases>pytest test_basic_authentication.py -s -v
# ========================================================================= test session starts =========================================================================
# platform win32 -- Python 3.8.2, pytest-7.4.4, pluggy-0.13.1 -- c:\python38\python.exe
# cachedir: .pytest_cache
# metadata: {'Python': '3.8.2', 'Platform': 'Windows-10-10.0.19041-SP0', 'Packages': {'pytest': '7.4.4', 'pluggy': '0.13.1'}, 'Plugins': {'allure-pytest': '2.13.2', 'html': '4.1.1', 'metadata': '3.0.0', 'xdist': '3.5.0'}}
# rootdir: C:\Users\hp\PycharmProjects\API_Student_Management_System\TestCases
# plugins: allure-pytest-2.13.2, html-4.1.1, metadata-3.0.0, xdist-3.5.0
# collected 1 item
#
# test_basic_authentication.py::test_basic_auth {"message":"Requires authentication","documentation_url":"https://docs.github.com/rest/users/users#get-the-authenticated-user"}
# PASSED
