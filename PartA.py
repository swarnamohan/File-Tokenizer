import sys

# Runs in linear time, based on number of characters in file which are read one by one
# This method is used in the tokenize method to obtain the next token in the giveen file
def get_next_token(file):
    token = ''

    while True:
        c = file.read(1)
        if len(c) == 0:
            if len(token) > 0:
                return token
            else:
                return None
            
        if c.isalnum() and c.isascii():
            token = token + c.lower()
        elif len(token) > 0:
            return token
        
        
# Runs in linear time, based on number of characters in file which are read one by one with get_next_token meethod
def tokenize(file_name):
    tokens = []
    with open(file_name, encoding='utf-8') as file:
        while True:
            token = get_next_token(file)
            if token != None:
                tokens.append(token)
            else:
                return tokens
            
    
# Runs in linear time, based on number of elements in the argument list which are added one by one to dictionary
def computeWordFrequencies(tokens):
    freq = {}
    for token in tokens:
        if token in freq:
            freq[token] = freq[token]+1  
        else: freq[token] = 1
             
    return freq


# Runs in linear time, based on number of keys in map which are printed one by one
def print_token(freq):
    for key,val in sorted(freq.items(), key=lambda keyval:(-keyval[1], keyval[0])):
        print(key+"\t"+str(val))
        

if __name__ == "__main__":
    
    print_token(computeWordFrequencies(tokenize(*sys.argv[1:])))
