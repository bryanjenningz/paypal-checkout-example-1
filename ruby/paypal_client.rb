require 'paypal-checkout-sdk'

module PayPalClient
  class << self

    # Set up and return PayPal Ruby SDK environment with PayPal access credentials.
    # This sample uses SandboxEnvironment. In production, use LiveEnvironment.
    def environment
      client_id = ENV['PAYPAL_CLIENT_ID'] || 'PAYPAL-SANDBOX-CLIENT-ID'
      client_secret = ENV['PAYPAL_CLIENT_SECRET'] || 'PAYPAL-SANDBOX-CLIENT-SECRET'

      PayPal::SandboxEnvironment.new(client_id, client_secret)
    end

    # Returns PayPal HTTP client instance with environment that has access
    # credentials context. Use this instance to invoke PayPal APIs, provided the
    # credentials have access.
    def client
      PayPal::PayPalHttpClient.new(self.environment)
    end
  end
end
