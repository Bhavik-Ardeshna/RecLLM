# import functions
from modules.encodings import fn_encoding
from llm.groq_client import fn_LLM
from modules.prompts import fn_prompts
from modules.main import fn_main

# import extra libraries
from groq import Groq
from sentence_transformers import SentenceTransformer

class agent(
    fn_encoding,
    fn_LLM,
    fn_prompts,
    fn_main
    ):

    def __init__(self, groq_api_key):
        client = Groq(
            api_key=groq_api_key #os.environ.get("GROQ_API_KEY"),
        )
        self.client = client
        self.model = SentenceTransformer('all-MiniLM-L6-v2') #all-MiniLM-L6-v2 #all-mpnet-base-v2