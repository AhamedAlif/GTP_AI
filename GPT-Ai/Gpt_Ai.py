import openai

# Set up your OpenAI API credentials
openai.api_key = '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'

# Define a function to interact with the AI chatbot
def chat_with_alva(user_input, chat_log=None):
    # Define the chat conversation prompt
    prompt = ""
    if chat_log is not None:
        prompt += chat_log
    prompt += f"You: {user_input}\nAlva:"

    # Make an API call to the GPT API
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        n=3,
        stop=None,
        timeout=15
    )

    # Extract the generated responses
    replies = [choice.text.strip().split("\n")[0] for choice in response.choices]

    # Filter and select the most suitable response based on intent
    selected_reply = filter_responses(user_input, replies)

    # Update the chat log with the new conversation
    chat_log += f"You: {user_input}\nAlva: {selected_reply}\n"

    return selected_reply, chat_log

# Define a function to filter responses based on intent
def filter_responses(user_input, replies):
    intent = determine_intent(user_input)

    if intent == 'greeting':
        filtered_replies = [reply for reply in replies if determine_intent(reply) != 'farewell']
    else:
        filtered_replies = replies

    return filtered_replies[0] if filtered_replies else "I'm sorry, I don't have a suitable response."

# Define a simple intent recognition function
def determine_intent(text):
    text = text.lower()
    if any(word in text for word in ['hello', 'hi', 'hey']):
        return 'greeting'
    elif any(word in text for word in ['bye', 'goodbye']):
        return 'farewell'
    else:
        return 'other'

# Example usage
chat_log = None

while True:
    user_input = input("You: ")

    if user_input.lower() == 'bye':
        print("Alva: Goodbye!")
        break

    response, chat_log = chat_with_alva(user_input, chat_log)
    print("Alva:", response)
