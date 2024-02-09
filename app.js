const openai = require('openai');
require('dotenv').config();
const express = require('express');
const path = require('path');
const app = express();
const port = 8080 || process.env.PORT;

app.use(express.json());
app.use(express.static('public'));
app.use(express.urlencoded({ extended: true }));

//Configure OpenAI
const configuration = new openai.Configuration({
    organization: process.env.OPENAI_ORG,
    apiKey: process.env.OPENAI_API_KEY,
});

const openaiapi = new openai.OpenAIApi(configuration);


app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '/index.html'));
});

app.post('/chat', async (req, res) => {
    const messages = req.body.messages;
    const model = req.body.model;
    const temp = req.body.temp;

    const completion = await openaiapi.createChatCompletion({
        model: model,
        messages: messages,
        temperature: temp,
    });
    res.status(200).json({ result: completion.data.choices });
});

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`);
});
