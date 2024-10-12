import requests

AUTH_SERVICE_URL = "http://localhost:8000"  # Update with your authentication service URL

def verify_token(token):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(f"{AUTH_SERVICE_URL}/user_account/api/user/", headers=headers)

    if response.status_code == 200:
        return response.json()  
    else:
        return None 

token = verify_token("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI3MjY1MTc1LCJpYXQiOjE3MjcyNjMzNzUsImp0aSI6ImIyZDQ5NDBiMDE4MTRmZjJiYzg2NjJjNjVlYWU5MDNkIiwidXNlcl9pZCI6Mn0.82hnx1_N3h38yPr6WD2Sy9KYLpuPVSc8SuUkOKipThU")

#test if auth_service works
print(token)