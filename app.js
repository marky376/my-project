const express = require('express');
const cors = require('cors');
const app = express();
const port = 3000;

// CORS options
const corsOptions = {
  origin: 'http://example.com', // allow only this origin
  methods: 'GET,POST', // allow only these methods
  allowedHeaders: 'Content-Type,Authorization' // allow only these headers
};

// Use CORS middleware with options
app.use(cors(corsOptions));

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});

