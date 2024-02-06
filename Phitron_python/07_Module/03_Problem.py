""" import pyjokes

joke = pyjokes.get_joke(language="en",category="neutral")


print(pyjokes)
 """
 
""" import pyjokes

def tell_some_jocks():
    
    while True:
        print("\nHello! I'm Your Joke Telling ChatBot. Type 'joke' to get a jock & Type 'E' for exit")
        
        user_input = input("You : ")
        
        if user_input.lower() == 'E':
            print("Good Bye! Exit Done")
            break
        
        elif 'joke' in user_input.lower():
            joke = pyjokes.get_joke()
            print("Chatbot: "+ joke)
        else:
            print("Chatbot: I'm here to tell jokes. Type 'Joke' for a joke. ")
            
tell_some_jocks() """





# =================================================

import pyjokes

def tell_some_joeks():
    
    while True:
        
        print("\nI'm Your Joke ChatBot!\nType 'Joke' For Joke & Type 'S' for Stop")
        
        user_input = input("You: ")
        
        if user_input.lower() == 's':
            print("Good Bye! Stop Chatbot")
            break
        elif user_input.lower() in 'joke':
            joke = pyjokes.get_joke()
            print("Chatbot: ", joke)
        else:
            print("Type 'Joke' For Joke & Type 'S' for Stop")

tell_some_joeks()





































