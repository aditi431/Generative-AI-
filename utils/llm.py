
import os
from dotenv import load_dotenv
from google import genai


# Load environment variables from .env file
load_dotenv()


# Get Gemini API key
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")


# Create Gemini client
client = genai.Client(api_key=API_KEY)


def generate_answer(question, context):

    prompt = f"""
You are an AI assistant that answers questions based ONLY on
the information provided in the PDF context.

PDF CONTEXT:
{context}

USER QUESTION:
{question}

Instructions:
- Answer only using information from the PDF context.
- If the answer is not present in the context, say:
  "I could not find this information in the uploaded PDF."
- Do not make up information.
- Explain the answer clearly and simply.
"""

    # Send the prompt to Gemini
    response = client.interactions.create(
        model="gemini-3.6-flash",
        input=prompt
    )

    # Return Gemini's answer
    return response.output_text

