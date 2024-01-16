import requests
import json
import jsonpath
def test_add_new_student():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails"
    file = open("C:\\Users\\hp\\PycharmProjects\\API_Student_Management_System\\TestCases\\RequestJson.json", "r")
    request_json = json.loads(file.read())
    response = requests.post(API_URL,request_json)
    print(response.text)

def test_get_student_data():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/10056954"
    response = requests.get(API_URL)
    print(response.text)
    response_json = json.loads(response.text)
    id = jsonpath.jsonpath(response_json,'data.id')
    print(id)
    assert id[0] ==10056954

# git remote add origin https://github.com/k-abhii/API_Student_Management_System_Testing_Python_Requests.git
# git branch -M main
# git push -u origin main

def test_update_details():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/10056954"
    f = open("C:/Users/hp/PycharmProjects/API_Student_Management_System/TestCases/PutRequest.json")
    request_json = json.loads(f.read())
    response = requests.put(API_URL,request_json)
    print(response.text)
#
# platform win32 -- Python 3.8.2, pytest-7.4.4, pluggy-0.13.1 -- c:\python38\python.exe
# cachedir: .pytest_cache
# metadata: {'Python': '3.8.2', 'Platform': 'Windows-10-10.0.19041-SP0', 'Packages': {'pytest': '7.4.4', 'pluggy': '0.13.1'}, 'Plugins': {'allure-pytest': '2.13.2', 'html': '4.1.1', 'metadata': '3.0.0', 'xdist': '3.5.0'}}
# rootdir: C:\Users\hp\PycharmProjects\API_Student_Management_System
# plugins: allure-pytest-2.13.2, html-4.1.1, metadata-3.0.0, xdist-3.5.0
# collected 3 items
#
# TestCases/test_AddNewStudent.py::test_add_new_student {"id":10056937,"first_name":"Testing","middle_name":"K","last_name":"World","date_of_birth":"12/12/1998"}
# PASSED
# TestCases/test_AddNewStudent.py::test_get_student_data {"status":"true","data":{"id":10056912,"first_name":"Testing","middle_name":"K","last_name":"World","date_of_birth":"12/12/1998"}}
# [10056912]
# PASSED
# TestCases/test_AddNewStudent.py::test_update_details {"status":"true","msg":"update  data success"}
# PASSED

# C:\Users\hp\PycharmProjects\API_Student_Management_System>pytest -s -v
# ========================================================================= test session starts =========================================================================
# platform win32 -- Python 3.8.2, pytest-7.4.4, pluggy-0.13.1 -- c:\python38\python.exe
# cachedir: .pytest_cache
# metadata: {'Python': '3.8.2', 'Platform': 'Windows-10-10.0.19041-SP0', 'Packages': {'pytest': '7.4.4', 'pluggy': '0.13.1'}, 'Plugins': {'allure-pytest': '2.13.2', 'html': '4.1.1', 'metadata': '3.0.0', 'xdist': '3.5.0'}}
# rootdir: C:\Users\hp\PycharmProjects\API_Student_Management_System
# plugins: allure-pytest-2.13.2, html-4.1.1, metadata-3.0.0, xdist-3.5.0
# collected 3 items
#
# TestCases/test_AddNewStudent.py::test_add_new_student {"id":10056938,"first_name":"Testing","middle_name":"K","last_name":"World","date_of_birth":"12/12/1998"}
# PASSED
# TestCases/test_AddNewStudent.py::test_get_student_data {"status":"true","data":{"id":10056912,"first_name":"Testing","middle_name":"K2","last_name":"The World","date_of_birth":"12/12/2000"}}
# [10056912]
# PASSED
# TestCases/test_AddNewStudent.py::test_update_details {"status":"true","msg":"update  data success"}
# PASSED

# Validating Data is updated or not using get request
def test_get_s_data():
    API_URL ="https://thetestingworldapi.com/api/studentsDetails/10056954"
    response = requests.get(API_URL)
    json_response = response.json()
    print(json_response)
    id = jsonpath.jsonpath(json_response,'data.id')
    print(id)
    assert id[0] ==10056954
    middle_name = jsonpath.jsonpath(json_response,'data.middle_name')
    assert middle_name[0] == "K2"
    dob = jsonpath.jsonpath(json_response,'data.date_of_birth')
    assert dob[0] == '12/12/2000'

# C:\Users\hp\PycharmProjects\API_Student_Management_System>pytest -s -v
# ================================================= test session starts =================================================
# platform win32 -- Python 3.8.2, pytest-7.4.4, pluggy-0.13.1 -- c:\python38\python.exe
# cachedir: .pytest_cache
# metadata: {'Python': '3.8.2', 'Platform': 'Windows-10-10.0.19041-SP0', 'Packages': {'pytest': '7.4.4', 'pluggy': '0.13.1'}, 'Plugins': {'allure-pytest': '2.13.2', 'html': '4.1.1', 'metadata': '3.0.0', 'xdist': '3.5.0'}}
# rootdir: C:\Users\hp\PycharmProjects\API_Student_Management_System
# plugins: allure-pytest-2.13.2, html-4.1.1, metadata-3.0.0, xdist-3.5.0
# collected 4 items
#
# TestCases/test_AddNewStudent.py::test_add_new_student {"id":10056951,"first_name":"Testing","middle_name":"K","last_name":"World","date_of_birth":"12/12/1998"}
# PASSED
# TestCases/test_AddNewStudent.py::test_get_student_data {"status":"true","data":{"id":10056912,"first_name":"Testing","middle_name":"K2","last_name":"The World","date_of_birth":"12/12/2000"}}
# [10056912]
# PASSED
# TestCases/test_AddNewStudent.py::test_update_details {"status":"true","msg":"update  data success"}
# PASSED
# TestCases/test_AddNewStudent.py::test_get_s_data {'status': 'true', 'data': {'id': 10056912, 'first_name': 'Testing', 'middle_name': 'K2', 'last_name': 'The World', 'date_of_birth': '12/12/2000'}}
# [10056912]
# PASSED
#
# ================================================== 4 passed in 4.85s ==================================================

def test_delete_student():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/10056954"
    response = requests.delete(API_URL)
    print(response.text)
    resposne_json = response.json()
    msg = jsonpath.jsonpath(resposne_json,'msg')
    print(msg[0])
    assert msg[0] == 'Delete  data success'
    status = jsonpath.jsonpath(resposne_json,'status')
    print(status[0])
    assert status[0] =="true"

# C:\Users\hp\PycharmProjects\API_Student_Management_System>pytest -s -v
# ========================================================================= test session starts =========================================================================
# platform win32 -- Python 3.8.2, pytest-7.4.4, pluggy-0.13.1 -- c:\python38\python.exe
# cachedir: .pytest_cache
# metadata: {'Python': '3.8.2', 'Platform': 'Windows-10-10.0.19041-SP0', 'Packages': {'pytest': '7.4.4', 'pluggy': '0.13.1'}, 'Plugins': {'allure-pytest': '2.13.2', 'html': '4.1.1', 'metadata': '3.0.0', 'xdist': '3.5.0'}}
# rootdir: C:\Users\hp\PycharmProjects\API_Student_Management_System
# plugins: allure-pytest-2.13.2, html-4.1.1, metadata-3.0.0, xdist-3.5.0
# collected 5 items
#
# TestCases/test_AddNewStudent.py::test_add_new_student {"id":10056952,"first_name":"Testing","middle_name":"K","last_name":"World","date_of_birth":"12/12/1998"}
# PASSED
# TestCases/test_AddNewStudent.py::test_get_student_data {"status":"true","data":{"id":10056912,"first_name":"Testing","middle_name":"K2","last_name":"The World","date_of_birth":"12/12/2000"}}
# [10056912]
# PASSED
# TestCases/test_AddNewStudent.py::test_update_details {"status":"true","msg":"update  data success"}
# PASSED
# TestCases/test_AddNewStudent.py::test_get_s_data {'status': 'true', 'data': {'id': 10056912, 'first_name': 'Testing', 'middle_name': 'K2', 'last_name': 'The World', 'date_of_birth': '12/12/2000'}}
# [10056912]
# PASSED
# TestCases/test_AddNewStudent.py::test_delete_student {"status":"true","msg":"Delete  data success"}
# PASSED
#
# ========================================================================== 5 passed in 3.00s ======

# C:\Users\hp\PycharmProjects\API_Student_Management_System>pytest -s -v
# ========================================================================= test session starts =========================================================================
# platform win32 -- Python 3.8.2, pytest-7.4.4, pluggy-0.13.1 -- c:\python38\python.exe
# cachedir: .pytest_cache
# metadata: {'Python': '3.8.2', 'Platform': 'Windows-10-10.0.19041-SP0', 'Packages': {'pytest': '7.4.4', 'pluggy': '0.13.1'}, 'Plugins': {'allure-pytest': '2.13.2', 'html': '4.1.1', 'metadata': '3.0.0', 'xdist': '3.5.0'}}
# rootdir: C:\Users\hp\PycharmProjects\API_Student_Management_System
# plugins: allure-pytest-2.13.2, html-4.1.1, metadata-3.0.0, xdist-3.5.0
# collected 5 items
#
# TestCases/test_AddNewStudent.py::test_add_new_student {"id":10056955,"first_name":"Testing","middle_name":"K","last_name":"World","date_of_birth":"12/12/1998"}
# PASSED
# TestCases/test_AddNewStudent.py::test_get_student_data {"status":"true","data":{"id":10056954,"first_name":"Testing","middle_name":"K","last_name":"World","date_of_birth":"12/12/1998"}}
# [10056954]
# PASSED
# TestCases/test_AddNewStudent.py::test_update_details {"status":"true","msg":"update  data success"}
# PASSED
# TestCases/test_AddNewStudent.py::test_get_s_data {'status': 'true', 'data': {'id': 10056954, 'first_name': 'Testing', 'middle_name': 'K2', 'last_name': 'The World', 'date_of_birth': '12/12/2000'}}
# [10056954]
# PASSED
# TestCases/test_AddNewStudent.py::test_delete_student {"status":"true","msg":"Delete  data success"}
# Delete  data success
# true
# PASSED
#
# ========================================================================== 5 passed in 1.14s ====
