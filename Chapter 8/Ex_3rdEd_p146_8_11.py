def show_messages(messages):
    """Print a list containing short text messages."""
    for message in messages:
        print(message)

messages = ["are you there?", "see you soon", "now-now"]
show_messages(messages)

def send_messages(messages, sent_messages):
    """Print each text message, and then move it to sent_messages."""
    print("\nSending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

sent_messages = []
send_messages(messages[:], sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)
