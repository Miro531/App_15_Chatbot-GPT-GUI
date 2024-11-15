import openai

class Chatbot:
    def __init__(self):
        openai.api_key = "sk-proj-Tvug2LkTLOvLDVjMixQ0T3BlbkFJkgYyVqqkfKWq8HLfC4DT"

    def get_response(self, user_input, max_tokens=150, temperature=0.5):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=max_tokens,
            temperature=temperature
        )
        return response.choices[0].message['content']

if __name__ == "__main__":
    chatbot = Chatbot()
    #response = chatbot.get_response("write a joke about birds")
    #print(response)
