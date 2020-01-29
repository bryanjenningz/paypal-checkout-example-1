require 'sinatra'
require_relative './handle_paypal_request'

get '/' do
  send_file File.expand_path('index.html', settings.public_folder)
end

post '/paypal-transaction-complete' do
  request.body.rewind  # in case someone already read it
  data = JSON.parse request.body.read
  Samples::GetOrder::new::get_order(data['orderID'])
end
