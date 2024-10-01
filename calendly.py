import requests


access_token = ''  # Replace with your personal access token
webhook_url = ''  # Replace with your server URL


#get uri
# Set up the headers
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

# Make the GET request to retrieve user details
response = requests.get('https://api.calendly.com/users/me', headers=headers)

# Check the response
if response.status_code == 200:
    user_info = response.json()
    print("User Information:", user_info)
    
    # Access the organization URI
    if 'organization' in user_info:
        organization_uri = user_info['organization']['uri']
        print("Your organization URI:", organization_uri)
    else:
        print("No organization found for this user.")
else:
    print(f"Error retrieving user details: {response.status_code} - {response.text}")

#create webhook
# Set up the headers and payload
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {access_token}'
}

data = {
    "url": webhook_url,
    "events": ["invitee.created"],
    "organization": organization_uri,
    "scope": "organization"
}

# Make the POST request to create the webhook subscription
response = requests.post('https://api.calendly.com/webhook_subscriptions', headers=headers, json=data)

# Check the response
if response.status_code == 201:
    print("Webhook subscription created successfully.")
else:
    print(f"Error creating webhook: {response.status_code} - {response.text}")