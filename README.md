# paypal-checkout-example
A simple working end-to-end PayPal checkout example

## Follow these steps to get everything working
- Make sure you have git installed and run the following commands in your terminal:
```
git clone https://github.com/paypal/paypal-checkout-example.git
cd paypal-checkout-example
```
- Open up checkout-example in your favorite text editor (like VSCode https://code.visualstudio.com/)
- Find/replace all instances of "PAYPAL-SANDBOX-CLIENT-ID" with your sandbox client ID found here when you create and view your app here: https://developer.paypal.com/developer/applications/
- Find/replace all instances of "PAYPAL-SANDBOX-CLIENT-SECRET" with your sandbox secret found here when you create and view your app here: https://developer.paypal.com/developer/applications/
- Run these commands to install NPM (Node.js Package Manager) dependencies and run the server:
```
npm install
npm run dev
```
- Go to http://localhost:3545 in your browser
- Test out PayPal Checkout by clicking the payment buttons and making a purchase with your sandbox account login credentials found here: https://developer.paypal.com/developer/accounts/
- You should see success messages in your browser console and in the terminal that's running your server
