# CSC289-Tax-Estimation-Service
Github repository for our tax estimation service class project.

Tax Estimation Service <br>
This project provides a simple Tax Estimation Service that calculates state and federal income taxes based on user input. Follow the instructions below to set up and run the project on your local machine.
<br> Prerequisites <br>
Make sure you have the following tools installed on your machine:

<br> Python (3.6 or higher)
<br> Pip
<br> Django
<br> Pytest
<br>
<br>
Clone the Repository <br>
<code>git clone https://github.com/Llamahawk/CSC289-Tax-Estimation-Service.git <br>
</code>
<code>cd CSC289-Tax-Estimation-Service/calculator_project
</code>

<br> Set Up Virtual Environment <br>
<code>python -m venv venv</code>
or
<code>python3 -m venv venv</code>

<br>Activate Virtual Environment<br>
On Windows: <code>venv\Scripts\activate</code>
On macOS/Linux: <code>source venv/bin/activate</code>

<br>Install Dependencies<br>
<code>pip install -r requirements.txt</code>
or
<code>pip3 install -r requirements.txt</code>

<br>Run migrations<br>
<code>python manage.py migrate</code>
or
<code>python3 manage.py migrate</code>


<br>Run the Development Server<br>
<code>python manage.py runserver</code>
or
<code>python3 manage.py runserver</code>

Visit http://127.0.0.1:8000 in your web browser to access the application.

<br>Running Tests<br>
<code>python -m pytest</code>
This command will run both unittests and pytests.


**If you need to add html / css files**

To customize the appearance of the Tax Estimation Service, you can modify the HTML and CSS files in the "templates" and "static" directories, respectively.

**Adding HTML Files**
Create New HTML Files:

Navigate to the calculator_app/templates directory.
Create new HTML files for your desired pages (e.g., custom_page.html).
Extend Base Template (Optional):

If you want to use a common structure across multiple pages, consider extending the base template.
In your HTML file, use the {% extends 'base.html' %} tag at the top.
Include CSS Files (Optional):

Include CSS files within the HTML file using the {% load static %} and {% static 'css/style.css' %} tags.

**Adding CSS Files**
Create New CSS Files:

Navigate to the calculator_app/static/css directory.
Create new CSS files for styling (e.g., custom_style.css).
Link CSS Files in HTML:

In your HTML file, link the CSS files using the <link> tag.
Example: <link rel="stylesheet" href="{% static 'css/custom_style.css' %}">
Apply Styling:

Write your custom styles in the CSS files to modify the appearance of the HTML elements.
Run the Development Server:

After making changes, run the development server (python manage.py runserver) to see the updated pages.

***Adding Automated Tests***

To ensure the reliability and correctness of the Tax Estimation Service, you can add automated tests using unittest and pytest.

**Using Unittest**
Create Test Files:

Navigate to the calculator_app/tests directory.
Create new Python files for your tests (e.g., test_calculator.py).
Write Test Cases:

In the test file, import the unittest module.
Define test cases by creating classes that inherit from unittest.TestCase.
Write test methods within these classes.
Run Unittests:

Open a terminal and run the following command:
<code> python -m unittest discover calculator_app.tests </code>
or
<code> python3 -m unittest discover calculator_app.tests </code>
Ensure that your tests pass without errors.

**Using Pytest**

Install Pytest:

If you haven't installed pytest, run the following command:

<code>pip install pytest</code>
or

<code>pip3 install pytest</code>

Create Test Files:

Similar to Unittest, create Python files for your tests (e.g., test_calculator.py).
Write Test Cases:

In the test file, write test functions using the def test_... syntax.
Run Pytests:

Open a terminal and run the following command:
<code>pytest calculator_app/tests</code>

Verify that your tests pass successfully.
Coverage (Optional):

To check test coverage, install the coverage tool:
<code>pip install coverage</code>
or
<code>pip3 install coverage</code>

Run the tests with coverage:
<code>coverage run -m pytest calculator_app/tests</code>

View the coverage report:
<code>coverage report -m</code>
![coverage_report](screenshots/coverage_report.png)

****Writing Front-End Tests****

If you want to write tests for front-end components, especially those involving POST requests, you can use tools like Selenium or Cypress. Here's a basic guide using Selenium:

Using Selenium for Front-End Tests

Install Selenium:

Ensure you have Selenium installed. You can install it using:
<code>pip install selenium</code>
or
<code>pip3 install selenium</code>

Download WebDriver:

Download the appropriate WebDriver for your browser (e.g., ChromeDriver, GeckoDriver).
Place the WebDriver executable in a directory included in your system's PATH.
Write Selenium Tests:

Create a new Python file for your Selenium tests (e.g., test_frontend.py).
Use the webdriver module from Selenium to simulate user interactions.
Write test cases that involve interacting with elements, submitting forms, and verifying results.
Example:

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

Run Selenium Tests:

Execute your Selenium tests using a command similar to:
```python -m unittest test_frontend.py```
or
```python3 -m unittest test_frontend.py```

Make sure the Django development server is running during the tests.
Continuous Integration (Optional):

Consider integrating Selenium tests into your continuous integration (CI) pipeline for automated testing.
Note:
Selenium tests interact with your application as if a real user would. Ensure your application is running during the tests.
Adjust the URLs and test scenarios based on your specific front-end components and functionality.

***Deploying Django Project to GitHub Pages***
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
input: choose and action and click the button (POST) <br>
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
