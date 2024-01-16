import requests
import json
import jsonpath
def test_add_data():
    APP_URL = "https://thetestingworldapi.com/api/studentsDetails"
    file = open("C:/Users/hp/PycharmProjects/API_Student_Management_System/TestCases/End_To_End_Post.json","r")
    request_json = json.loads(file.read())
    response = requests.post(APP_URL,request_json)
    print(response.text)
    id = jsonpath.jsonpath(response.json(),'id')
    print(id[0])
    tech_url = "https://thetestingworldapi.com/api/technicalskills"
    f = open("C:/Users/hp/PycharmProjects/API_Student_Management_System/TestCases/TechDetails.json", "r")
    request_js = json.loads(f.read())
    request_js['id'] = int(id[0])
    request_js['st_id'] = id[0]
    response = requests.post(tech_url,request_js)
    print(response.text)

    add_api_url = "https://thetestingworldapi.com/api/addresses"
    f2 = open("C:/Users/hp/PycharmProjects/API_Student_Management_System/TestCases/address.json","r")
    req_json = json.loads(f2.read())
    req_json['stId'] = id[0]
    res = requests.post(add_api_url,req_json)
    print(res.text)

    final_details = "https://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response = requests.get(final_details)
    print(response.text)

# C:\Users\hp\PycharmProjects\API_Student_Management_System\TestCases>pytest test_end_to_end.py -s
# ========================================================================= test session starts =========================================================================
# platform win32 -- Python 3.8.2, pytest-7.4.4, pluggy-0.13.1
# rootdir: C:\Users\hp\PycharmProjects\API_Student_Management_System\TestCases
# plugins: allure-pytest-2.13.2, html-4.1.1, metadata-3.0.0, xdist-3.5.0
# collected 1 item
#
# test_end_to_end.py {"id":10056975,"first_name":"Abhimanyu","middle_name":"M","last_name":"Kumar","date_of_birth":"14/12/1997"}
# 10056975
# {"status":"true","msg":"Add  data success"}
# {"status":"true","msg":"Add  data success"}
# {"status":"true","data":{"first_name":"Abhimanyu","middle_name":"M","last_name":"Kumar","date_of_birth":"14/12/1997","TechnicalDetails":[{"id":756203,"language":["Python","Javascript"],"yearexp":"2.5","lastused":"2024","st_id":"10056960"},{"id":756204,"language":["Python","Javascript"],"yearexp":"2.5","lastused":"2024","st_id":"10056960"},{"id":756205,"language":["Python","Javascript"],"yearexp":"2.5","lastused":"2024","st_id":"10056960"},{"id":756206,"language":["Python","Javascript"],"yearexp":"2.5","lastused":"2024","st_id":"10056960"}],"Address":[{"Permanent_Address":{"House_Number":null,"City":null,"State":null,"Country":null,"PhoneNumber":null},"Current_Address":null,"stId":"10056960"},{"Permanent_Address":{"House_Number":null,"City":null,"State":null,"Country":null,"PhoneNumber":null},"Current_Address":null,"stId":"10056960"},{"Permanent_Address":{"House_Number":null,"City":null,"State":null,"Country":null,"PhoneNumber":null},"Current_Address":null,"stId":"10056960"},{"Permanent_Address":{"House_Number":null,"City":null,"State":null,"Country":null,"PhoneNumber":null},"Current_Address":null,"stId":"10056960"},{"Permanent_Address":{"House_Number":null,"City":null,"State":null,"Country":null,"PhoneNumber":null},"Current_Address":null,"stId":"10056960"},{"Permanent_Address":{"House_Number":null,"City":null,"State":null,"Country":null,"PhoneNumber":null},"Current_Address":null,"stId":"10056960"}]}}

# C:\Users\hp\PycharmProjects\API_Student_Management_System\TestCases>pytest test_end_to_end.py -s
# ========================================================================= test session starts =========================================================================
# platform win32 -- Python 3.8.2, pytest-7.4.4, pluggy-0.13.1
# rootdir: C:\Users\hp\PycharmProjects\API_Student_Management_System\TestCases
# plugins: allure-pytest-2.13.2, html-4.1.1, metadata-3.0.0, xdist-3.5.0
# collected 1 item
#
# test_end_to_end.py {"id":10056986,"first_name":"Abhimanyu","middle_name":"M","last_name":"Kumar","date_of_birth":"14/12/1997"}
# 10056986
# {"status":"true","msg":"Add  data success"}
# {"status":"true","msg":"Add  data success"}
# {"status":"true","data":{"first_name":"Abhimanyu","middle_name":"M","last_name":"Kumar","date_of_birth":"14/12/1997","TechnicalDetails":[{"id":756208,"language":["Python","Javascript"],"yearexp":"2.5","lastused":"2024","st_id":"10056986"}],"Address":[{"Permanent_Address":{"House_Number":null,"City":null,"State":null,"Country":null,"PhoneNumber":null},"Current_Address":null,"stId":"10056986"},{"Permanent_Address":{"House_Number":null,"City":null,"State":null,"Country":null,"PhoneNumber":null},"Current_Address":null,"stId":"10056986"}]}}
# .
#
# ========================================================================== 1 passed in 1.29s ==========================================================================
