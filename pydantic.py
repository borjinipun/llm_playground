agent = Agent('groq:llama-3.3-70b-versatile')

from dotenv import load_dotenv
import os

load_dotenv()

from pydantic_ai import Agent
from pydantic_ai.models.groq import GroqModel
from pydantic_ai.providers.groq import GroqProvider

model = GroqModel(
    'llama-3.3-70b-versatile', provider=GroqProvider(api_key=os.getenv('GROQ_API_KEY'))
)
agent = Agent(model)