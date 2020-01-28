# 1. Import the PayPal SDK client that was created in `Set up Server-Side SDK`.
from paypalclient import PayPalClient
from paypalcheckoutsdk.orders import OrdersGetRequest


class GetOrder(PayPalClient):
    # 2. Set up your server to receive a call from the client
    """You can use this function to retrieve an order by passing order ID as an argument"""

    def get_order(self, order_id):
        """Method to get order"""
        request = OrdersGetRequest(order_id)
        # 3. Call PayPal to get the transaction
        response = self.client.execute(request)
        # 4. Save the transaction in your database. Implement logic to save transaction to your database for future reference.
        print('Status Code: ', response.status_code)
        print('Status: ', response.result.status)
        print('Order ID: ', response.result.id)
        print('Intent: ', response.result.intent)
        formatted_amount = '{} {}'.format(response.result.purchase_units[0].amount.currency_code,
                                          response.result.purchase_units[0].amount.value)
        print('Gross Amount: {}', formatted_amount)
        print('Links:')
        for link in response.result.links:
            print('\t{}: {}\tCall Type: {}'.format(
                link.rel, link.href, link.method))
        if response.status_code == 200:
            return {'status': 200, 'message': 'Transaction complete', 'amount': formatted_amount}
        return {'status': response.status_code, 'message': 'Non-200 status code returned'}
