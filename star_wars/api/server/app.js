const express = require('express');
require('./database');
const cors = require('cors');


const app = express()

// Settings
const port = process.env.PORT || 4000;
app.set('port', port);


// Middlewares
app.use(express.json());
app.use(cors());

// Routes
app.use('/api/star-wars', require('./routes/characters'));



app.listen(app.get('port'), function() {
    console.log('Server running on port ' + app.get('port'));
});