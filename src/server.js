const express = require('express');
const handlePaypalRequest = require('./handlePaypalRequest');

const app = express();
app.use(express.json());

app.get('/', (req, res) => {
  res.sendFile(`${__dirname}/index.html`);
});

app.post('/paypal-transaction-complete', handlePaypalRequest);

const port = process.env.PORT || 3545;
app.listen(port, () => {
  console.log(`Listening on port ${port}`);
});
