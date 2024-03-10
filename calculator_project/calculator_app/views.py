import json

import bcrypt
from django.shortcuts import render, redirect
from django.views import View

from .models.user import User


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
        user = next((user for user in user_data_list if user['email_address'] == email), {})

        try:
            if user and bcrypt.checkpw(password.encode('utf-8'), user['hashed_password'].encode('utf-8')):
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
                    'hashed_password': user_instance.hashed_password,
                })

                # Write the updated data back to the file
                with open(self.user_dictionary, 'w') as file:
                    json.dump(user_data_list, file)

                # Redirect to a success page or another view
                return redirect('signup_success')
            except ValueError as e:
                # Handle validation errors
                return render(request, self.template_name, {'error_message': str(e)})

