def print_texts(messages):
    for message in messages:
        print(message)

def send_messages(messages, message_board):
    while messages:
        sent_message = messages.pop()
        print (f"adding '{sent_message}' to sent messages list.")
        message_board.append(sent_message)


texts = ['your great', 'missing you', "what's up", 'howdy']
sent_messages = []

print_texts(texts)
send_messages(texts[:], sent_messages)

print (texts)
print (sent_messages)