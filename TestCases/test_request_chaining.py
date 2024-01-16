import requests
import json
import jsonpath
def test_add_student_details():
    global id
    api_url = "https://thetestingworldapi.com/api/studentsDetails"
    file = open("C:/Users/hp/PycharmProjects/API_Student_Management_System/TestCases/request_chaining.json","r")
    request_json = json.loads(file.read())
    response = requests.post(api_url,request_json)
    print(response.text)
    id = jsonpath.jsonpath(response.json(),'id')
    print(id[0])
def test_get_details():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/"+str(id[0])
    response = requests.get(API_URL)
    print(response.text)

# C:\Users\hp\PycharmProjects\API_Student_Management_System\TestCases>pytest test_request_chaining.py -s
# ========================================================================= test session starts =========================================================================
# platform win32 -- Python 3.8.2, pytest-7.4.4, pluggy-0.13.1
# rootdir: C:\Users\hp\PycharmProjects\API_Student_Management_System\TestCases
# plugins: allure-pytest-2.13.2, html-4.1.1, metadata-3.0.0, xdist-3.5.0
# collected 2 items
#
# test_request_chaining.py {"id":10057012,"first_name":"Abhimanyu","middle_name":"Hare","last_name":"Kumar","date_of_birth":"14/12/1997"}
# 10057012
# .{"status":"true","data":{"id":10057012,"first_name":"Abhimanyu","middle_name":"Hare","last_name":"Kumar","date_of_birth":"14/12/1997"}}
# .
#
# ========================================================================== 2 passed in 3.75s ==========================================================================
#
# C:\Users\hp\PycharmProjects\API_Student_Management_System\TestCases>