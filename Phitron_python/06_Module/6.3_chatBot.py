""" 
    ChatBot
    * input / listen
    * process / decide
    * output / talkback

"""
greet_words = ['hi','hello','yoo']
bye_words = ['bye','tata']

def listen():
    return input("Say Something: ")

def decide(command):
    # print(command)
    broken_words = command.split(" ")
    # print(broken_words)
    
    command = command.lower()

    for words in broken_words:
        if words in greet_words:
            talkback("he said Greetings")
            break
            
        if words in bye_words:
            talkback("He Said bye")
            break
        
def talkback(response):
    print(response)


command = listen()
decide(command)



































