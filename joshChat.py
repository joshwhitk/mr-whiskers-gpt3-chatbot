import openai


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

openai.api_key = open_file('openaiapikey.txt')

def gpt3_completion(prompt, engine='text-davinci-002', temp=0.7, top_p=1.0, tokens=400, freq_pen=0.0, pres_pen=0.0, stop=['USER:']):
    prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temp,
        max_tokens=tokens,
        top_p=top_p,
        frequency_penalty=freq_pen,
        presence_penalty=pres_pen,
        stop=stop)
    text = response['choices'][0]['text'].strip()
    # add a string to text in spanish




    return text

if __name__ == '__main__':
    conversation = list()
    print()
    print("This is a simple tool to chat with 'Mr. Cat', a GPT-3 powered character that discusses children's books. Type 'exit' to quit.")
    print()
    while True:
        user_input = input('USER: ')
        conversation.append('USER: %s' % user_input)
        text_block = '\n'.join(conversation)
        prompt = open_file('prompt_chat.txt').replace('<<BLOCK>>',text_block)
        prompt = prompt + '\nCAT:'        
        response = gpt3_completion(prompt)
        conversation.append('JAX: %s' % response)
        print(response)
  

print()
print("This is a simple tool to chat with 'Mr. Cat', a GPT-3 powered character that discusses children's books. Type 'exit' to quit.")
print()
  