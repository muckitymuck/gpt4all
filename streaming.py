from flask import Flask, request, Response
from gpt4all import GPT4All

app = Flask(__name__)
model = GPT4All(model_name='ggml-model-gpt4all-falcon-q4_0.bin')

@app.route('/generate', methods=['POST'])
def generate_response():
    prompt = request.json['prompt']
    responses = []

    def generate_tokens():
        with model.chat_session():
            tokens = model.generate(prompt=prompt, top_k=1, streaming=True)
            response = ''.join(tokens)
            responses.append(response)
            yield response

    return Response(generate_tokens(), content_type='text/plain')

if __name__ == '__main__':
    app.run()


from flask import Flask, request, Response
from gpt4all import GPT4All

app = Flask(__name__)
model = GPT4All(model_name='ggml-model-gpt4all-falcon-q4_0.bin')

@app.route('/generate', methods=['POST'])
def generate_response():
    prompts = request.json['prompts']
    responses = []

    def generate_tokens():
        for prompt in prompts:
            with model.chat_session():
                tokens = model.generate(prompt=prompt, streaming=True)
                response = ''.join(tokens)
                responses.append(response)
                yield response

    return Response(generate_tokens(), content_type='text/plain')

if __name__ == '__main__':
    app.run()
