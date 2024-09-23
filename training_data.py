import json
import random


# Load the JSON data
def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


# Get a random response for an intent
def get_intent_response(intent, data):
    responses = data["intents"]
    for item in responses:
        if item['tag'] == intent:
            return random.choice(item['responses'])
    return random.choice(data['intents'][-1]['responses'])


# chatbot
def main():
    data = load_data('responses.json')
    print("Chatbot: Hi! How can I help you today?")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        else:
            # Check user input
            found = False
            for intent in data['intents']:
                for pattern in intent['patterns']:
                    if user_input.lower() == pattern.lower():
                        print("Chatbot:", get_intent_response(intent['tag'], data))
                        found = True
                        break
                if found:
                    break
            if not found:
                print("Chatbot:", random.choice(data['intents'][-1]['responses']))  # default


# Run the chatbot
if __name__ == "__main__":
    main()
