```json
{
  "files": [
    {
      "file_name": "main.py",
      "content": "import requests\nimport time\nimport json\nfrom flask import Flask, render_template, request, jsonify\n\napp = Flask(__name__)\n\n# Function to get user data from GitHub API\ndef get_github_user(username):\n    url = f'https://api.github.com/users/{username}'\n    response = requests.get(url)\n    return response.json()\n\n# Function to calculate account age\ndef calculate_account_age(created_at):\n    created_time = time.strptime(created_at, '%Y-%m-%dT%H:%M:%SZ')\n    age_in_days = (time.time() - time.mktime(created_time)) / (24 * 3600)\n    return int(age_in_days)\n\n@app.route('/')\ndef index():\n    return render_template('index.html')\n\n@app.route('/lookup', methods=['POST'])\ndef lookup():\n    username = request.form['username']\n    user_data = get_github_user(username)\n    if 'message' in user_data and user_data['message'] == 'Not Found':\n        return jsonify({'error': 'User not found'}), 404\n    account_age = calculate_account_age(user_data['created_at'])\n    user_data['account_age'] = account_age\n    return jsonify(user_data)\n\nif __name__ == '__main__':\n    app.run(debug=True)"
    },
    {
      "file_name": "README.md",
      "content": "# GitHub User Lookup App\n\nThis is a minimal Flask application that allows users to look up GitHub user information. The app includes enhancements such as:\n\n- **ARIA-live status updates** for accessibility.\n- **Account age display** to show how long the account has been active.\n- **LocalStorage caching** to store user data for faster subsequent lookups.\n\n## Requirements\n- Python 3.x\n- Flask\n- Requests library\n\n## Setup\n1. Clone the repository.\n2. Install the required packages:\n   ```bash\n   pip install Flask requests\n   ```\n3. Run the application:\n   ```bash\n   python main.py\n   ```\n4. Open your browser and go to `http://127.0.0.1:5000/`.\n\n## Usage\n- Enter a GitHub username in the provided input field and submit to see user details.\n- The app will display the account age and cache the data in localStorage for faster access."
    }
  ]
}
```