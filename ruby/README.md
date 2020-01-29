# ruby-paypal-checkout-example

A simple working end-to-end PayPal checkout example

## Follow these steps to get everything working

- Make sure you have git installed and run the following commands in your terminal:

```
git clone https://github.com/paypal/paypal-checkout-example.git
cd paypal-checkout-example/ruby
```

- Open up checkout-example in your favorite text editor (like VSCode https://code.visualstudio.com/)
- Find/replace all instances of "PAYPAL-SANDBOX-CLIENT-ID" with your sandbox client ID found here when you create and view your app here (you will need to log in with your business PayPal account): https://developer.paypal.com/developer/applications/
- Find/replace all instances of "PAYPAL-SANDBOX-CLIENT-SECRET" with your sandbox secret found here when you create and view your app here (you will need to log in with your business PayPal account): https://developer.paypal.com/developer/applications/
- Run these commands to install Ruby gems and run the Ruby Sinatra server:

```
gem install sinatra paypal-checkout-sdk
ruby server.rb
```

- Go to http://localhost:4567 in your browser
- Test out PayPal Checkout by clicking the payment buttons and making a purchase with your sandbox account login credentials found here: https://developer.paypal.com/developer/accounts/
- You should see success messages in your browser console and in the terminal that's running your server
