const redis = require('redis');
const { promisify } = require('util');

const client = redis.createClient();
client.on('error', (err) => console.log('Redis client not connected to the server:', err));
client.on('ready', () => console.log('Redis client connected to the server'));

function setNewSchool (schoolName, value) {
  client.set(schoolName, value, redis.print);
}

const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue (schoolName) {
  try {
    const reply = await getAsync(schoolName);
    console.log(reply);
  } catch (err) {
    console.error(err);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
