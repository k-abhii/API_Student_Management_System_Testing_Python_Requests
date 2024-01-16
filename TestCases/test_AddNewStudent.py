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
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/10056912"
    response = requests.get(API_URL)
    print(response.text)
    response_json = json.loads(response.text)
    id = jsonpath.jsonpath(response_json,'data.id')
    print(id)
    assert id[0] ==10056912

