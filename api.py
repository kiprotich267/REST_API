from flask import Flask,jsonify
import requests

app = Flask(__name__)

API_URL = "https://jsonplaceholder.typicode.com"
@app.route('/')
def home():
    return "Welcome to the API!"
#routes for getting all posts
@app.route('/posts')
def get_posts():
    response = requests.get(f"{API_URL}/posts")
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch posts"}), 404
    return jsonify(response.json())


#routes for getting users
@app.route('/users')
def get_all_users():
    response = requests.get(f"{API_URL}/users")
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch users"}), 404
    return jsonify(response.json())

@app.route('/users/<int:user_id>',methods={'GET'})
def get_user(user_id):
    response = requests.get(f"{API_URL}/users/{user_id}")
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch user's posts"}), 404
    user_data = response.json()
    return jsonify(user_data)

#getting posts 
@app.route('/users/<int:user_id>/posts')
def get_user_posts(user_id):
    response = requests.get(f"{API_URL}/users/{user_id}/posts")
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch users' posts"}), 404
    user_data = response.json()
    return jsonify(user_data)




if __name__=="__main__":
    app.run(debug=True)