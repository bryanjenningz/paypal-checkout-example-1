from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
import sys


class PayPalClient:
    def __init__(self):
        self.client_id = "PAYPAL-SANDBOX-CLIENT-ID"
        self.client_secret = "PAYPAL-SANDBOX-CLIENT-SECRET"

        """Set up and return PayPal Python SDK environment with PayPal access credentials.
           This sample uses SandboxEnvironment. In production, use LiveEnvironment."""

        self.environment = SandboxEnvironment(
            client_id=self.client_id, client_secret=self.client_secret)

        """ Returns PayPal HTTP client instance with environment that has access
            credentials context. Use this instance to invoke PayPal APIs, provided the
            credentials have access. """
        self.client = PayPalHttpClient(self.environment)
