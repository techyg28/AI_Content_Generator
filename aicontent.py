import os # provide functions for creating and removing directory, fetching its content, changing and
# identifying the current directory
import openai  # It is a library we are doing everthing with
import config  # config file contains the key
openai.api_key = config.OPENAI_API_KEY # initializing the key

def openAIQuery(query):
    response = openai.Completion.create(
        engine = "davinci-instruct-beta",
        prompt= query,
        temperature = 0.5,
        max_tokens = 200,
        top_p = 1,
        frequency_penalty=0,
        presence_penalty=0)
    
    # This query passes a resopnse object but we only need first object of choices array and its text part.
    # (If no result come back)
    # For handling exception we have to check that choices should be present in the response 
    # otherwise return string like 'Opps sorry, you beat the AI this time'
    if 'choices' in response:
        if len(response['choices']) > 0:
            answer = response['choices'][0]['text']
        else:
            answer = 'Opps sorry, you beat the AI this time'
    else:
        answer = 'Opps sorry, you beat the AI this time'
        
    return answer




        # response = openai.Completion.create(
        # model="davinci-instruct-beta",
        # prompt="Generate a detailed product description for apple iphone\n\n",
        # temperature=0.5,
        # max_tokens=200,
        # top_p=1,
        # frequency_penalty=0,
        # presence_penalty=0) 
