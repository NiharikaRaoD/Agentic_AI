from typing import TypedDict
from dotenv import load_dotenv
import os

class Email(TypedDict):
    Draft_Email: str
    Email_Tone: str
    Final_Email: str

load_dotenv()
model_name = os.getenv('MODEL_NAME')

