from dotenv import load_dotenv
import os
from strands import Agent
from tool import calculate_expression

load_dotenv()

MODEL_NAME = os.environ.get("MODEL_NAME")
SERVER_URL = os.environ.get("SERVER_URL")

agent = Agent(
    model=MODEL_NAME,
    tools=[calculate_expression],
    model_url=SERVER_URL,
)
