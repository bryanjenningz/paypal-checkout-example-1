'use strict';

/**
 *
 * PayPal Node JS SDK dependency
 */
const checkoutNodeJssdk = require('@paypal/checkout-server-sdk');

/**
 *
 * Returns PayPal HTTP client instance with environment that has access
 * credentials context. Use this instance to invoke PayPal APIs, provided the
 * credentials have access.
 */
function client() {
  return new checkoutNodeJssdk.core.PayPalHttpClient(environment());
}

/**
 *
 * Set up and return PayPal JavaScript SDK environment with PayPal access credentials.
 * This sample uses SandboxEnvironment. In production, use LiveEnvironment.
 *
 */
function environment() {
  /**
   *
   * Change the clientId value below to your sandbox client ID for testing.
   * Change the clientSecret value below to your sandbox client secret for testing.
   * You can change them to your live client ID and secret once you're ready for production.
   * You can find your sandbox client ID and secret here: https://developer.paypal.com/developer/applications
   * You can click "Sandbox", then click "Create App", then click on the app to get the client ID and secret
   * and paste it here as the values.
   */
  const clientId = process.env.PAYPAL_CLIENT_ID || 'PAYPAL-SANDBOX-CLIENT-ID';
  const clientSecret =
    process.env.PAYPAL_CLIENT_SECRET || 'PAYPAL-SANDBOX-CLIENT-SECRET';

  // In live, change this call to LiveEnvironment instead of SandboxEnvironment
  return new checkoutNodeJssdk.core.SandboxEnvironment(clientId, clientSecret);
}

module.exports = { client: client };
