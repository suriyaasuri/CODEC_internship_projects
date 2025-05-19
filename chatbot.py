from transformers import pipeline

# Using a basic conversational pipeline
chatbot_pipeline = pipeline("conversational", model="microsoft/DialoGPT-small")

def get_response(user_input):
    from transformers import Conversation
    conversation = Conversation(user_input)
    result = chatbot_pipeline(conversation)
    return result.generated_responses[-1]