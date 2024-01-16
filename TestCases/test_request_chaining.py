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