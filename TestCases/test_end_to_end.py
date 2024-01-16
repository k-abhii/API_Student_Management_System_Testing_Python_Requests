import requests
import json
import jsonpath
def test_add_data():
    APP_URL = "https://thetestingworldapi.com/api/studentsDetails"
    file = open("C:/Users/hp/PycharmProjects/API_Student_Management_System/TestCases/End_To_End_Post.json","r")
    request_json = json.loads(file.read())
    response = requests.post(APP_URL,request_json)
    print(response.text)

