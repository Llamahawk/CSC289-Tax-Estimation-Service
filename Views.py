# views.py
from django.shortcuts import render, redirect

# This list will act as an in-memory storage for user data
user_data_list = []

def index(request):
    if request.method == 'POST':
        user_data = {
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
            'email': request.POST.get('email'),
            'password': request.POST.get('password'),
            'income': request.POST.get('income'),
            'tax_id': request.POST.get('tax_id'),
            'filing_status': request.POST.get('filing_status'),
        }

        user_data_list.append(user_data)
        return redirect('success')  # Redirect to a success page

    return render(request, 'index.html')

def success(request):
    return render(request, 'success.html', {'user_data_list': user_data_list})
