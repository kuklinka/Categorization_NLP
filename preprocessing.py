import re
def process(input):
    input=input.lower()
    input=re.sub(r'[^0-9a-zA-Z ]','',input)
    input=input.replace('\n','')
    return input