from dotenv import load_dotenv
import os
from strands.agent import Agent
from strands.models.ollama import OllamaModel
from tool import calculate_expression

load_dotenv()

MODEL_NAME = os.environ.get("MODEL_NAME")
SERVER_URL= os.environ.get("SERVER_URL")

ollama_model = OllamaModel(
    host=SERVER_URL,
    model_id=MODEL_NAME
)

agent = Agent(
    model=ollama_model,
    tools=[calculate_expression]
)
