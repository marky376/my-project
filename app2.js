// Load environment variables from .env file
require('dotenv').config();

const express = require('express');
const cors = require('cors');
const axios = require('axios'); // require axios
const app = express();

// Use the environment variable PORT or default to 3000
const port = process.env.PORT || 3000;

// Use CORS middleware
app.use(cors());

app.get('/', (req, res) => {
  res.send('Hello World!');
});

// Example route that uses Axios to fetch data from an external API
app.get('/api/data', async (req, res) => {
  try {
    const response = await axios.get('https://api.example.com/data');
    res.json(response.data);
  } catch (error) {
    res.status(500).json({ message: 'Error fetching data', error: error.message });
  }
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});

