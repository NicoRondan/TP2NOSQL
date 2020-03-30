const redis = require('redis');

const redisClient = redis.createClient(6379, 'redis');

redisClient.on('connect', () => {
    console.log('Connected to redis server')
});

module.exports = {redisClient};