const { Client } = require('g4f'); // Import your GPT package

export default async function handler(req, res) {
    // Get the 'prompt' query parameter from the URL
    const prompt = req.query.prompt || 'Hello';

    // Create a client instance and send the prompt to GPT
    const client = new Client();
    const response = await client.chat.completions.create({
        model: 'gpt-3.5-turbo',  // Use 'gpt-4' if supported
        messages: [{ role: 'user', content: prompt }]
    });

    // Extract and return the generated response content
    const result = response.choices[0].message.content;
    
    // Return the result as JSON
    res.status(200).json({ result });
}
