const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json);

app.use(express.static('frontend'))

app.get('/', (req, res) => {
    res.sendFile('/frontend/index.html');
})

app.listen(8800, ()=>{
    console.log('sapana Server started on port 8800 ')
})
