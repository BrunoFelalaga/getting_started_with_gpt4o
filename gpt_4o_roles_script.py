
import os
import openai
from openai import AzureOpenAI

def setup_client(vendor='openAI', api_key=None, azure_endpoint=None):
    if vendor == 'azure':
        return AzureOpenAI(
            azure_endpoint=azure_endpoint,
            api_key=api_key,
            api_version='2024-06-01'
        )
    elif vendor == 'openAI':
        openai.api_key = api_key
        return openai
    else:
        raise ValueError('Unknown AI API')

def get_completion(client, system_prompt, user_prompt, model="gpt-4", temperature=0.2):
    completion = client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return completion.choices[0].message.content

def main():
    # Configure your API key here
    api_key = userdata.get('OpenAIAPIKey2') #os.getenv('OPENAI_API_KEY')
    client = setup_client(api_key=api_key)
    
    # Example prompts
    prompts = {
        "standard": "You are a helpful assistant.",
        "physicist": "You are a helpful assistant and a PhD in Physics and speaking in terms of physics at every turn. It shows in your every sentence you utter and you only see the world through physics",
        "preschool": "You are a helpful assistant well versed with breaking concepts down for pre-schoolers. You will explain everything as though the user was a 6 year old",
        "pirate": "You are a helpful assistant and only speak in medieval pirate english. You will explain everything as though you are a medieval pirate in the middle of a thundering storm and angry to be bothered with trivial questions"
    }
    
    # Test each role
    for role, system_prompt in prompts.items():
        print(f"\n=== Testing {role.upper()} role ===")
        response = get_completion(
            client,
            system_prompt,
            "Tell me the story of the frog and scorpion briefly"
        )
        print(response)
        print("\n" + "="*50)

if __name__ == "__main__":
    main()
