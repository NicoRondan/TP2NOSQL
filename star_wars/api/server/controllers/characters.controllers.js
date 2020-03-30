const characterCtrl = {};
const {redisClient} = require('../database');

characterCtrl.getCharacters =  async (req, res) => {
    //Extraigo parametros de la url
    const {episode} = req.params;
    //Obtengo personajes del episodio
    await redisClient.lrange(episode, 0, -1, (err, values) => {
        if (!err) {
            res.json(values);
            console.log(values);
        } else {
            res.json('An error has occurred');
            console.log(err);
        }
    }); 

};

characterCtrl.createCharacter = async (req, res) =>{
    //Extraigo parametros de la url
    const {episode, character} = req.params;
    //Inserto el pj con su respectivo episodio
    await redisClient.lpush(episode, character);
    //Muestro por consola la lista
    await redisClient.lrange(episode, 0, -1, (err, values) => {
        if (!err) {
            res.json('Character created');
            console.log(values);
        } else {
            res.json('An error has occurred');
            console.log(err);
        }
    });   
};

characterCtrl.deleteCharacter = async (req, res) => {
    //Extraigo parametros de la url
    const {episode, character} = req.params;
    await redisClient.lrem(episode, 0, character, (err, reply) => {
        if (!err) {
            res.json('Character deleted');
            //console.log(reply);
        } else {
            res.json('An error has occurred');
            console.log(err);
        }
    }); 
};

module.exports = characterCtrl;