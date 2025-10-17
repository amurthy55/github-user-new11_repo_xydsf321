from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

HTML_TEMPLATE = '''<!doctype html>\n<html lang='en'>\n<head>\n    <meta charset='UTF-8'>\n    <meta name='viewport' content='width=device-width, initial-scale=1.0'>\n    <link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css'>\n    <title>GitHub User Fetcher</title>\n</head>\n<body>\n<div class='container'>\n    <h1>Fetch GitHub User Creation Date</h1>\n    <form id='github-user-{{ seed }}' method='GET'>\n        <div class='form-group'>\n            <label for='username'>GitHub Username:</label>\n            <input type='text' class='form-control' id='username' name='username' required>\n        </div>\n        <div class='form-group'>\n            <label for='token'>Token (optional):</label>\n            <input type='text' class='form-control' id='token' name='token'>\n        </div>\n        <button type='submit' class='btn btn-primary'>Fetch</button>\n    </form>\n    <div id='github-created-at' class='mt-3'></div>\n</div>\n<script>\n    document.getElementById('github-user-{{ seed }}').onsubmit = async function(event) {\n        event.preventDefault();\n        const username = document.getElementById('username').value;\n        const token = document.getElementById('token').value;\n        const response = await fetch(`https://api.github.com/users/${username}${token ? `?access_token=${token}` : ''}`);\n        const data = await response.json();\n        const createdAt = data.created_at ? new Date(data.created_at).toISOString().split('T')[0] : 'User not found';\n        document.getElementById('github-created-at').innerText = `Account Creation Date: ${createdAt}`;\n    };\n</script>\n</body>\n</html>'''

@app.route('/', methods=['GET'])
def index():
    seed = 1  # You can change this to any seed value you want
    return render_template_string(HTML_TEMPLATE, seed=seed)

if __name__ == '__main__':
    app.run(debug=True)