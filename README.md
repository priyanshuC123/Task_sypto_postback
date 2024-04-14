# Webhook Task with Flask API and FYERS Integration

## Overview
This project involves creating a Flask API to handle webhook requests from FYERS (a broker API) and sending emails using Mailtrap. When an order is placed in FYERS, it triggers a webhook to a specified endpoint in our Flask API (/fyers route). The Flask API then processes the request and sends an email notification to the desired recipient using Mailtrap's services.

## Usage
1. **Hosting the Application**: Firstly, you need to host the Flask application. Ensure that the application is hosted and accessible via a base URL.
   
2. **Setting Up Webhook**: Use the base URL of your hosted application as the base URL for the webhook/postback URL in FYERS. Set the route to `/fyers`. This ensures that FYERS triggers the webhook URL whenever an order is placed.

3. **Email Notification**: The Flask API handles the incoming webhook requests and sends an email using Mailtrap's services to the specified recipient email address.

## Testing
To test the functionality:
- Use `http://127.0.0.1:5000/fyers` as the webhook link if you're testing locally (assuming Flask is running on the default port 5000).
- Ensure that Mailtrap is properly configured with the Flask API to capture and display the sent emails.
- Place a test order in FYERS to trigger the webhook and observe the email notification sent to the recipient address.

## Note
- This is a basic application designed for demonstration purposes.
- Make sure to replace placeholders with actual values (e.g., email addresses, API keys) before deploying the application in a production environment.
