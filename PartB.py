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
            
        if c.isalnum():
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


# Runs in linear time, as the tokenize function is used in this function, which goes through one character at a time in the given files
def common_tokens (file1, file2):
    file1_tokens = tokenize(file1)
    file2_tokens = tokenize(file2)
    
    common_set = set(file1_tokens).intersection(set(file2_tokens))
    
    print(len(common_set))


if __name__ == "__main__":
    
    common_tokens(sys.argv[1],sys.argv[2])
    
