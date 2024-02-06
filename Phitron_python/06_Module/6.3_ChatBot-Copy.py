""" 
    ChatBot
    * input / listen
    * process / decide
    * output / talkback

"""
Greeting_word = ['hi','hello','yoo']
bye_words = ['tata','bye']

def listen():
    return input("Say Something: ")

def decide(command):
    broken_word = command.split(" ")
    command = command.lower()
    
    for words in broken_word:
        if words in Greeting_word:
            talkBack("He Said Greetings")
            break
        
        if words in bye_words:
            talkBack("He Said Bye")
            break    

def talkBack(response):
    print(response)

command = listen()
decide(command)