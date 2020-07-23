# Resolve the problem!!
import re


def run():
    # Start coding here
    letters = []
    with open('encoded.txt', 'r', encoding='utf-8') as f:
    # code
        
         # reading each line     
        for line in f: 
    
            # reading each word         
            for word in line.split(): 
    
                # agg each lower case letter in letters            
                matches = re.findall(r'[a-z]+', word)
                letters.append(matches)  
    
    
    hiden_word = ''.join(letters[0])
    print(f'El mensaje oculto es {hiden_word}')

if __name__ == '__main__':
    run()
