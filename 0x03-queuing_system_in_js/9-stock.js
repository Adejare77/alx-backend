const express = require('express');
const redis = require('redis');

const app = express();
const port = 1245;

const listProducts = [
  {
    id: 1,
    name: 'Suitcase 250',
    price: 50,
    stock: 4,
  },
  {
    id: 2,
    name: 'Suitcase 450',
    price: 100,
    stock: 10,
  },
  {
    id: 3,
    name: 'Suitcase 650',
    price: 350,
    stock: 2,
  },
  {
    id: 4,
    name: 'Suitcase 1050',
    price: 550,
    stock: 5,
  }
]

function getItemById(id) {
  for (const item in listProducts) {
    if (item.id === id) {
      return item;
    }
  }
}


app.get('/list_products', (req, res) => {
  res.status(200).send(JSON.stringify(listProducts));
})


app.listen(port, () => {
  console.log('Server running on port 1245');
})

const client = redis.createClient();
client.on('connect', () => console.log('Redis client connected to the Server'))
client.on('error', () => console.log('Redis client NOT connected to the Server'))

function resevedStockById(itemId, stock) {
  client.set(itemId, stock);
}

async function getCurrentReservedStockById(itemId) {
  for (const item of listProducts) {
    if (item.id === ParseInt(itemId)) {
      return item.stock;
    }
  }
  return new Error('Not found');
}

app.get('/list_products/:itemId', (req, res) => {
  const itemId = req.params.itemId
  getCurrentReservedStockById(itemId)
  .then((item) => {
    res.status(200).send(JSON.stringify(item))
  }).catch((error) => {
    res.status(404).json({status: "Product not found"});
  })

})
