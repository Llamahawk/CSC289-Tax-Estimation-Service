import json
import bcrypt
from django.shortcuts import render, redirect
from django.views import View
from calculator_project.calculator_app.models.filing_status import FilingStatus
from .models.user import User
from calculator_project.calculator_app.services.tax_calculator import calculate_taxes


class MainView(View):
    template_name = 'calculator_app/main.html'

    def get(self, request):
        return render(request, self.template_name)


class LoginView(View):
    template_name = 'calculator_app/login.html'
    user_dictionary = 'user-dictionary.json'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Load user data from JSON file
        with open(self.user_dictionary, 'r') as file:
            user_data_list = json.load(file)

        # Check if user with given email exists
        user = next((user for user in user_data_list if user['email'] == email), {})

        try:
            if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
                # Authentication successful, redirect to dashboard or another page
                return redirect('dashboard')
            else:
                # Authentication failed, handle accordingly
                raise ValueError('Invalid credentials')
        except ValueError as e:
            # Handle authentication failure gracefully
            return render(request, self.template_name, {'error_message': str(e)})


class SignUpView(View):
    template_name = 'calculator_app/signup.html'  # Create a signup.html template
    user_dictionary = 'user-dictionary.json'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        # Handle user registration, hash password, etc.
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email_address = request.POST.get('email_address')
        password = request.POST.get('password')

        # Load existing user data from JSON file
        try:
            with open(self.user_dictionary, 'r') as file:
                user_data_list = json.load(file)
        except FileNotFoundError:
            # If the file doesn't exist, initialize an empty list
            user_data_list = []

        # Check if user with the same email already exists
        if any(user['email_address'] == email_address for user in user_data_list):
            return render(request, self.template_name, {
                'error_message': 'User with this email address already exists. Redirect to login page instead?'})
        else:
            # Validate and save user data
            try:
                user_instance = User(first_name, last_name, email_address, password)

                user_data_list.append({
                    'first_name': user_instance.first_name,
                    'last_name': user_instance.last_name,
                    'email_address': user_instance.email_address,
                    'password': user_instance.password,
                })

                # Write the updated data back to the file
                with open(self.user_dictionary, 'w') as file:
                    json.dump(user_data_list, file)

                # Redirect to a success page or another view
                return redirect('signup_success')
            except ValueError as e:
                # Handle validation errors
                return render(request, self.template_name, {'error_message': str(e)})


class DashboardView(View):
    template_name = 'calculator_app/dashboard.html'

    def get(self, request):
        # Check if the user is authenticated or redirect to login
        if not request.user.is_authentificated:
            return redirect('login')

        # Assuming you have a User model, you can get the user instance
        user_instance = request.user

        # Render the dashboard template with the user instance
        return render(request, self.template_name, {'user_instance': user_instance})

    def post(self, request):
        # Handle the tax calculation and update the tax_result variable
        # Assuming you have a function or method to calculate tax in your tax_calculator.py

        # Get selected filing status from the form
        filing_status_value = int(request.POST.get('filing_status', 0))
        filing_status = FilingStatus(filing_status_value)
        income = float(request.POST.get('income', 0.0))

        # Calculate tax using calculate_taxes function
        state_tax, fed_tax, total_tax = calculate_taxes(income, filing_status)

        # Get the user instance
        user_instance = request.user  # Adjust this based on your actual user retrieval logic

        # Render the dashboard template with the user instance and tax result
        return render(
            request, self.template_name, {
                'user_instance': user_instance,
                'state_tax': state_tax,
                'fed_tax': fed_tax,
                'total_tax': total_tax,
            }
        )
