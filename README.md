# GPT Role Playing Demo

This repository demonstrates GPT-4's ability to adapt to different roles and personalities through system prompts.

## Setup
```python
pip install openai
```

## Configuration
The notebook supports both OpenAI and Azure OpenAI endpoints:

```python
if vendor=='azure':
    client = AzureOpenAI(
        azure_endpoint=userdata.get('AzureAIEndpoint'),
        api_key=userdata.get('AzureAIKey'),
        api_version='2024-06-01'
    )
elif vendor=='openAI':
    openai.api_key = userdata.get('OpenAIAPIKey')
    client = openai
```

## Examples

### 1. Standard Response
A basic prompt asking about the fable of the frog and scorpion.

### 2. Physics Professor
The same story told through the lens of a physics PhD, incorporating physics concepts and analogies.

### 3. Pre-school Teacher
Explaining rainbow formation to a 6-year-old, using simple language and relatable analogies.

### 4. Medieval Pirate
Responding to philosophical questions in pirate vernacular during a storm.

## Key Findings

1. Role Adherence: GPT-4 maintains character while staying focused on the core question
2. Quality Control:
   - Best results: GPT-4 with temperature 0.2
   - Lower quality with:
     - Models below GPT-4
     - Temperature above 0.2 
3. Age-Appropriate Language: GPT-4 effectively adapts vocabulary and concepts for different age groups

## Usage

1. Set up your OpenAI/Azure credentials
2. Run the notebook cells sequentially
3. Experiment with different roles and prompts

## Requirements
- Python 3.x
- OpenAI package
- IPython
