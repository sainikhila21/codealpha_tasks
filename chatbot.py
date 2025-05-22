import nltk
from nltk.chat.util import Chat, reflections

# Define more patterns and responses
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!", "Howdy!", "Greetings!"]],
    [r"how are you?", ["I'm doing well, thanks!", "Great! How about you?", "Feeling awesome today!"]],
    [r"i am fine|i am good|i'm good|i'm fine", ["Glad to hear that!", "Awesome!", "That's great!"]],
    [r"what is your name?", ["I'm a chatbot created in Python.", "Call me PyBot!", "I'm just your friendly chatbot."]],
    [r"what do you do?", ["I chat with people!", "I'm here to have a good conversation.", "Helping you is what I do best!"]],
    [r"who created you?", ["I was coded by a human who loves Python.", "A Python developer brought me to life."]],
    [r"what can you do?", ["I can chat with you and keep you company!", "Right now, I'm learning to be more helpful."]],
    [r"tell me a joke", ["Why don’t scientists trust atoms? Because they make up everything!", 
                         "Why did the computer go to therapy? It had too many bugs.", 
                         "Why do programmers prefer dark mode? Because light attracts bugs!"]],
    [r"do you like (.*)?", ["I don't have preferences, but I think %1 is interesting!", 
                            "I can't experience feelings, but people talk a lot about %1."]],
    [r"i like (.*)", ["Nice! A lot of people like %1 too.", "That's cool. %1 is quite popular."]],
    [r"bye|goodbye|see you", ["Goodbye!", "See you later!", "Bye! Take care.", "Have a great day!"]],
    [r"(.) your favorite (.)", ["I don't have favorites, but %2 sounds great!", "I'm just code, but %2 seems fun!"]],
    [r"can you help me with (.*)", ["I'll do my best to help you with %1.", "Sure! Let's talk about %1."]],
    [r"(.*)", ["Tell me more...", "Interesting!", "Can you elaborate?", "Why do you say that?", "Hmm... that's something to think about."]],
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Start conversation
print("Hi! I'm PyBot 🤖. Let's chat! (Type 'bye' to exit)")
chatbot.converse()