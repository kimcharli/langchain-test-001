import openai

def parse_openai_api_key_file(penai_key_file = '/Users/ckim/.ssh/openai-google-key'):
    '''Parse the openai api key file and set the openai.api_key and openai.organization'''
    with open(penai_key_file, 'r') as f:
        for line in f.readlines():
            key = line.split('Authorization: Bearer ')
            if len(key) > 1:
                openai.api_key = key[1].strip()
            else:
                organization = line.split('OpenAI-Organization: ')    
                if len(organization) > 1:
                    openai.organization = organization[1].strip()
    # parse_openai_api_key_file(OPENAI_API_KEY_FILE)

