
# RecLLM
RecLLM: Recommendation using LLM &amp; RAG
=======
**Agent Engine - Complementary Products Discovery Engine**

**README FILE**

The Agent Engine is a Python-based artificial intelligence (AI) engine designed to discover complementary products for a given product. This engine utilizes natural language processing (NLP) and machine learning (ML) techniques to generate a list of products that are likely to be purchased together.

**STRUCTURE**

The code is structured into multiple files, each responsible for a specific task:

* `agent.py`: The main class responsible for initializing the engine and handling requests.
* `functions/prompts.py`: Contains classes for generating prompts for the large language model (LLM).
* `functions/main.py`: Contains classes for searching similar products, finding complementary candidates, and filtering complementary candidates.
* `functions/LLM.py`: Contains classes for integrating different LLMs.
* `functions/encoding.py`: Contains classes for encoding products and uploading encoded products.

**CONFIG FILE**

The API key for the Groq AI service is stored in a YAML configuration file named `config.yaml`. This file is used to configure the engine and provide the necessary credentials.

**USAGE**

To use the Agent Engine, follow these steps:

1. Install the required dependencies by running `pip install -r requirements.txt`.
2. Create a YAML configuration file named `config.yaml` with the following format:

```yaml
groq_api_key: YOUR_GROQ_API_KEY
```

Replace `YOUR_GROQ_API_KEY` with your actual Groq API key.
3. Run the engine by executing the Python script `agent.py` with the following command:

```
python agent.py
```

4. Provide the product name(s) as input to the engine, and it will return a list of complementary products.

**EXAMPLE OUTPUT**

The engine will return a pandas dataframe containing the following columns:

* `index`: The index of the complementary product.
* `product_name`: The name of the complementary product.
* `llm_product`: The product name used to generate the recommendation.
* `recommended_product`: The recommended product.
* `reasoning`: The reasoning behind the recommendation.
* `similarity_score`: The similarity score between the input product and the recommended product.
* `score`: The likelihood of purchasing the recommended product.
>>>>>>> master
