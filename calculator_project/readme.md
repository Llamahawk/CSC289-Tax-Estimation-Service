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