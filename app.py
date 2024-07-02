from flask import Flask, render_template_string, request
import re

app = Flask('_name_')

# HTML template
html_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Login Page</title>
    <script>
        function validateEmail(email) {
            const re = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,6}$/;
            return re.test(email);
        }

        function login() {
            const userId = document.getElementById('userId').value;
            const password = document.getElementById('password').value;

            if (!validateEmail(userId)) {
                alert("Please enter a valid email address.");
                return false;
            }

            if (password === "") {
                alert("Please enter a password.");
                return false;
            }

            return true;
        }
    </script>
</head>
<body>
    <div id="loginForm">
        <h2>Welcome to Innovagic Pvt Ltd. Please login to access benefits</h2>
        <form action="/login" method="post" onsubmit="return login()">
            <label for="userId">User ID:</label><br>
            <input type="text" id="userId" name="userId"><br><br>
            <label for="password">Password:</label><br>
            <input type="password" id="password" name="password"><br><br>
            <button type="submit">Login</button><br><br>
            <a href="#">Forgot password</a> 
            <a href="#">Register now</a>
        </form>
    </div>
</body>
</html>
'''

welcome_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Welcome</title>
</head>
<body>
    <h2>Welcome: {{ user_id }}</h2>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(html_template)
@app.route('/login', methods=['POST'])
def login():
    user_id = request.form['userId']
    password = request.form['password']

    # Validate email
    if not re.match(r"[^@]+@[^@]+\.[^@]+", user_id):
        return "Invalid email format. Please go back and try again."

    if not password:
        return "Password cannot be empty. Please go back and try again."

    # Redirect to welcome page
    return render_template_string(welcome_template, user_id=user_id)

if '_name_' == '_main_':
    app.run(debug=True, port=5001)