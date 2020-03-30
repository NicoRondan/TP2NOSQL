const {Router} = require('express');
const router = Router();
const {getCharacters, createCharacter, deleteCharacter} = require('../controllers/characters.controllers');


router.route('/:episode')
    .get(getCharacters)


router.route('/:episode/:character')
    .post(createCharacter)
    .delete(deleteCharacter)

module.exports = router;