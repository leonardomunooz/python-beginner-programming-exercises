# ✅↓ Write your code here ↓✅
letra = ['let it be', 'let it be', 'let it be', 'let it be', 'there will be an answer', 'let it be', 'let it be', 'let it be', 'let it be', 'let it be', 'whisper words of wisdom, let it be']


def sing():
    song = ''
    for i,reproduce in enumerate(letra):
        if i != len(letra) - 1:
            song += f"{reproduce},\n"
        else:
            song += f"{reproduce}"
    return song 
       
  


print(sing())