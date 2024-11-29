from flask import request, Flask, abort
import requests

app = Flask(__name__)

BASE_URL = "https://innovationcampus.ru/store/user"

@app.route("/store/user", methods=['GET', 'PUT', 'POST', 'DELETE'])
def query():
    if request.method == 'GET':
        response = requests.get(BASE_URL, params={"id": request.args["id"]})
        if response.status_code == 200:
            return response.json()
        else:
            abort(404)
    if request.method == 'PUT':
        response = requests.put(BASE_URL, json={
                                                "id": request.data["id"],
                                                "userName": request.data["userName"],
                                                "password": request.data["password"],
                                                "firstName": request.data["firstName"],
                                                "lastName": request.data["lastName"],
                                                "telephone": request.data["telephone"]})
        if response.status_code == 200:
            return response.json()
        else:
            abort(404)

    if request.method == 'POST':
        response = requests.post(BASE_URL, json={
                                                "id": request.args["id"],
                                                "userName": request.data["userName"],
                                                "password": request.data["password"],
                                                "firstName": request.data["firstName"],
                                                "lastName": request.data["lastName"],
                                                "telephone": request.data["telephone"]})
        if response.status_code == 200:
            return response.json()
        else:
            abort(404)
        
    if request.method == 'DELETE':
        response = requests.delete(BASE_URL, params={"id": request.args["id"]})
        if response.status_code == 200:
            return response.json()
        else:
            abort(404)

if __name__ == "__main__":
	app.run(port=8888)