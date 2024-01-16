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
    response = requests.post(tech_url,request_js)
    print(response.text)

    add_api_url = "https://thetestingworldapi.com/api/addresses"
    f2 = open("C:/Users/hp/PycharmProjects/API_Student_Management_System/TestCases/address.json","r")
    req_json = json.loads(f2.read())
    res = requests.post(add_api_url,req_json)
    print(res.text)

    filal_details = "https://thetestingworldapi.com/api/FinalStudentDetails/10056960"
    response = requests.get(filal_details)
    print(response.text)






