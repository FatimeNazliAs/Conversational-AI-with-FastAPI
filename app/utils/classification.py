import openai
import os

from dotenv import load_dotenv

load_dotenv()


openai.api_key = os.getenv("OPEN_AI_KEY")


def get_openAI_message_response(content, model="gpt-4o"):
    messages = [{"role": "user", "content": content}]
    try:
        response = openai.chat.completions.create(model=model, messages=messages)
        return response.choices[0].message.content.strip()
    except Exception as e:
        # Log the error and handle gracefully
        print(f"Error in OpenAI API call: {e}")
        return None


def classify_message(content):
    prompt = f"""
    Determine if the comment between three backticks can be classified as food or weather.
    '''{content}'''
    Provide answer as 'food' or 'weather'.
    """
    try:
        # Get the classification response from OpenAI
        answer = get_openAI_message_response(prompt, model="gpt-4o")
        # Validate the result
        if answer and answer.lower() in ["food", "weather"]:
            return answer.lower()
        else:
            raise ValueError("Unexpected classification result.")
    except Exception as e:
        # Log the error for debugging
        print(f"Error during classification: {e}")
        return "error"
