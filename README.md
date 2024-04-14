<h1>CSC289-Tax-Estimation-Service</h1>
Github repository for our tax estimation service class project.

<h2>Tax Estimation Service</h2> <br>
This project provides a simple Tax Estimation Service that calculates state and federal income taxes based on user input. Follow the instructions below to set up and run the project on your local machine.

<br> **Prerequisites:**<br>

<ul>
<br> <li>Python (3.6 or higher)</li>
<br> <li>Pip</li>
<br> <li>Django</li>
<br> <li>Pytest</li>
</ul>

<br>**Clone the Repository**<br>
<code>git clone https://github.com/Llamahawk/CSC289-Tax-Estimation-Service.git <br>
</code>
<code>cd CSC289-Tax-Estimation-Service/calculator_project
</code>

<br> **Set Up Virtual Environment** <br>
<code>python -m venv venv</code>
or
<code>python3 -m venv venv</code>

<br>**Activate Virtual Environment**<br>
On Windows: <code>venv\Scripts\activate</code><br>
On macOS/Linux: <code>source venv/bin/activate</code>

<br>**Install Dependencies**<br>
<code>pip install -r requirements.txt</code>
or
<code>pip3 install -r requirements.txt</code>

<br>**Run migrations**<br>
<code>python manage.py migrate</code>
or
<code>python3 manage.py migrate</code>


<br>**Run the Development Server**<br>
<code>python manage.py runserver</code>
or
<code>python3 manage.py runserver</code>

Visit http://127.0.0.1:8000/calculator_app/ in your web browser to access the application.

<br>**Running Tests**<br>
This command will run both unittests and pytests.<br>
<code>python -m pytest</code>



<h3>If you need to add html / css files:</h3>
<ol>
    <li>To customize the appearance of the Tax Estimation Service:</li>
        <ul>
            <li>Adding HTML Files:</li>
                <ul>
                    <li>Navigate to the 'calculator_app/templates' directory.</li>
                    <li>Create new HTML files for your desired pages(e.g., 'custom_page.html')</li>
                    <li>Optional: Extend base template by using '{% extends 'base.html' %}' tag in your HTML file.</li>
                    <li>Optional: Include CSS files within the HTML file using '{% load static %}' and '{% static 'css/style.css' %}' tags</li>
                </ul>
            <li>Adding CSS Files</li>
                <ul>
                    <li>Navigate to 'calculator_app/static/css' directory.</li>
                    <li>Create new CSS files for styling (e.g., 'custom_style.css').</li>
                    <li>Link CSS files in HTML files using the link tag.</li>
                    <li>Write your custom styles in the CSS files to modify the appearance of the HTML elements.</li>
                </ul>
            <li>Run the Development Server:</li>
                <ul>
                    <li>After making changes, run the development server ('python manage.py runserver') to see the updated pages.</li>
                </ul>
        </ul>
</ol>
<br>
<h3>Adding Automated Tests</h3>
<ol>
    <li>Using Unittest:</li>
        <ul>
            <li>Create test files in 'calculator_app/tests' directory.</li>
            <li>Write test cases using 'unittest' module.</li>
            <li>Run unittests:<br> <code>python -m unittest discover calculator_app.tests</code> 
                <br> or <br> 
                <code>python3 -m unittest discover calculator_app.tests</code></li>
        </ul>
    <li>Using Pytest:</li>
        <ul>
            <li>Install pytest if not already installed: <br>
            <code>pip install pytest</code>
            <br> or <br>
            <code>pip3 install pytest</code></li>
            <li>Write test files and test cases.</li>
            <li>Run Pytests:<br>
            <code>pytest calculator_app/tests</code></li>
            <li>Optional: Check test coverage using coverage tool.</li>
            <li>Run the tests with coverage:<br>
                <code>coverage run -m pytest calculator_app/tests</code></li>
            <li>View coverage report:<br>
            <code>coverage report -m</code></li>
        </ul><br>
<h3>Writing Front-End Tests</h3>
    <ol>
        <li>Using Selenium for Front-End Tests:
            <ul>
                <li>Ensure Selenium is installed:<br>
                <code>pip install selenium</code><br>
                or<br>
                <code>pip3 install selenium</code></li>
                <li>Download and place appropriate WebDriver in your system's PATH.<br>
                <li>Write Selenium tests simulating user interactions.</li>
            </ul>
    </ol>

```{python}
    from selenium import webdriver
    
    class FrontEndTests(unittest.TestCase):
        def setUp(self):
        self.driver = webdriver.Chrome()  # Use appropriate WebDriver
        
        def test_user_login(self):
            self.driver.get("http://localhost:8000/login")  # Adjust URL as needed
            # Simulate user interactions (e.g., filling forms, clicking buttons)
            # Assert the expected results
        
        def tearDown(self):
            self.driver.quit()
    
    if __name__ == "__main__":
        unittest.main()`
```

<h3>Run Selenium Tests</h3>

<ol>
    <li>Run your Selenium tests using this command:<br>
        <code>python -m unittest test_frontend.py</code>
        <br>or<br>
        <code>python3 -m unittest test_frontend.py</code>
    </li>
    <li>Ensure that the Django development server is running while running the tests.</li>
    <li>Optional: Consider integrating Selenium tests into your continuous integration (CI) pipeline for automated testing. Note that Selenium tests simulate real user         interactions with your application, so make sure your application is running during the tests. Adjust the URLs and test scenarios according to your specific front-end      components and functionality.</li>
</ol>


<h3>Deploying Django Project to GitHub Pages</h3>

```

Deploying a Django project to GitHub Pages isn't a straightforward task, as GitHub Pages is designed primarily for static websites, and Django is a full-stack web framework. However, you can host the static part of your project, such as HTML, CSS, and JavaScript files, on GitHub Pages, while deploying the Django backend separately. Here's a basic guide:

Deploying Front-End (HTML, CSS, JS) to GitHub Pages
Create a Separate Repository for Front-End:

Create a new GitHub repository specifically for hosting the front-end part of your project.
Push Front-End Files:

Push your HTML, CSS, and JS files to the GitHub repository you created in step 1.
Configure GitHub Pages:

In your GitHub repository, go to the "Settings" tab.
Scroll down to the "GitHub Pages" section.
Choose the branch that contains your front-end files (e.g., main or master).
GitHub Pages will automatically deploy your front-end at a URL like https://yourusername.github.io/repository-name.
Deploying Django Backend
Deploying the Django backend involves using a hosting service that supports Django applications. Popular choices include Heroku, PythonAnywhere, and AWS.

Example Deployment with Heroku:
Create a Heroku Account:

Sign up for a free Heroku account at Heroku.
Install Heroku CLI:

Install the Heroku Command Line Interface (CLI) on your local machine.
Login to Heroku:

Open a terminal and run:
bash
Copy code
heroku login
Create requirements.txt:

List all the Python packages required for your Django project in a requirements.txt file.
Create Procfile:

Create a file named Procfile (without any file extension) with the following content:
makefile
Copy code
web: gunicorn your_project_name.wsgi
Initialize Git Repository:

If you haven't initialized a Git repository, run the following commands:
bash
Copy code
git init
git add .
git commit -m "Initial commit"
Create a Heroku App:

Run the following command to create a new Heroku app:
bash
Copy code
heroku create your-unique-app-name
Push to Heroku:

Push your Django project to Heroku:
bash
Copy code
git push heroku master
Migrate Database:

Run database migrations on Heroku:
bash
Copy code
heroku run python manage.py migrate
Open the App:

Open your deployed Django app in the browser:
bash
Copy code
heroku open
Note:
GitHub Pages is suitable for static content, while the Django backend needs a separate hosting solution.
This guide focuses on deploying the front-end to GitHub Pages and the Django backend to Heroku. Adjust the steps based on your preferred hosting services.
```
url: http://127.0.0.1:8000/calculator_app/ <br>
input: choose an action and click the button (POST) <br>
expected result: redirects to 'login' or 'signup' <br>
![main_page.png](screenshots/main_page.png) <br>

url: http://127.0.0.1:8000/calculator_app/signup/ <br>
input: no input (GET) <br>
expected result: observing an empty 'signup' after redirection <br>
Placeholders in place <br>
![signup_empty.png](screenshots/signup_empty.png) <br>

url: http://127.0.0.1:8000/calculator_app/signup/ <br>
input: (POST) ![existing_user_input.png](screenshots/existing_user_input.png) <br>
expected result: User found in data dictionary <br>
Error "Email address already in use" is displayed <br>
Optional redirection to 'login' screen <br>
observing an empty 'signup' after rendering <br>
Placeholders in place <br>
![existing_user_output.png](screenshots/existing_user_output.png) <br>

url: http://127.0.0.1:8000/calculator_app/signup/ <br>
input: (POST) ![invalid_email_address_input.png](screenshots/invalid_email_address_input.png) <br>
expected result: Email validation failed <br>
"Invalid email address format" error is present <br>
User not created (not added to data-dictionary.json) <br>
observing an empty 'signup' after rendering <br>
![invalid_email_address_output.png](screenshots/invalid_email_address_output.png) <br>

url: http://127.0.0.1:8000/calculator_app/signup/ <br>
input: (POST) ![bad_password_input.png](screenshots/bad_password_input.png) <br>
expected result: Password validation failed <br>
"Password must be at least 8 character long" error is present <br>
User not created (not added to data-dictionary.json) <br>
observing an empty 'signup' after rendering <br>
![invalid_email_address_output.png](screenshots/bad_password_output.png) <br>

url: http://127.0.0.1:8000/calculator_app/signup/ <br>
input: (POST) ![good_signup_input.png](screenshots/good_signup_input.png) <br>
expected result: No errors <br>
User created (added to data-dictionary.json) <br>
Observing an empty 'dashboard' after redirect <br>
Ideally, user's first_name and last_name should be there
![good_signup_output.png](screenshots/good_signup_output.png) <br>

url: http://127.0.0.1:8000/calculator_app/login/ <br>
input: right credentials (good@email.com Pa$$w0rd) <br>
(POST) ![login_existing_user_right_password_input.png](screenshots/login_existing_user_right_password_input.png) <br>
expected result: No errors <br>
Observing an empty 'dashboard' after redirect <br>
Ideally, user's first_name and last_name should be there
![login_existing_user_right_password_output.png](screenshots/login_existing_user_right_password_output.png) <br>

url: http://127.0.0.1:8000/calculator_app/login/ <br>
input: user not registered (bad@email.com any password) <br>
(POST) ![login_bad_user_input.png](screenshots/login_bad_user_input.png) <br>
expected result: No user found <br>
System suggests to signup instead <br>
![login_bad_user_output.png](screenshots/login_bad_user_output.png) <br>

url: http://127.0.0.1:8000/calculator_app/login/ <br>
input: invalid password (good@email.com any password) <br>
(POST) ![invalid_credentials_input.png](screenshots/invalid_credentials_input.png) <br>
expected result: User found <br>
System suggests to think harder <br>
Add "forgot my password" later <br>
![invalid_credentials_output.png](screenshots/invalid_credentials_output.png) <br>

url: http://127.0.0.1:8000/calculator_app/dashboard/ <br>
input:50,000, then click "Calculate My Tax Liability" <br>
expected result: error. Please match the requested format. <br>
![dashboard_income_comma.png](screenshots/dashboard_income_comma.png) <br>

input: $50000, then click "Calculate My Tax Liability" <br>
expected result: error. Please match the requested format. <br>
![dashboard_dollar_sign_income.png](screenshots/dashboard_dollar_sign_income.png) <br>

input: -50000, then click "Calculate My Tax Liability" <br>
expected result: error. Please match the requested format. <br>
![dashboard_negative_income.png](screenshots/dashboard_negative_income.png) <br>

input: 60000.75, then click "Calculate My Tax Liability" <br>
expected result: Calculates correctly, numbers match pytest case <br>
desired outcome: user is passed from login/signup to dashboard view <br>
first_name and last_name are displayed <br>
![dashboard_good.png](screenshots/dashboard_good.png) <br>
