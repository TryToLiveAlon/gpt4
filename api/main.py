from flask import Flask, request, jsonify
from g4f.client import Client

app = Flask(__name__)

@app.route('/gpt4')
def gpt4():
    # Get the 'prompt' query parameter
    prompt = request.args.get('prompt', default="Hello", type=str)
    
    # Initialize the client and send the prompt to GPT-3.5-turbo (or GPT-4-like)
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4",  # Use GPT-4 here if available in g4f
        messages=[{"role": "user", "content": prompt}]
    )
    
    # Extract the generated response content
    result = response.choices[0].message.content
    
    return jsonify(result=result)

if __name__ == "__main__":
    app.run()
  
