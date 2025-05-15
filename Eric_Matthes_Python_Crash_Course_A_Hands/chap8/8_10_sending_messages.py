# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. 
# Write a function called send_messages() that prints each text message and 
# moves each message to a new list called sent_messages as it’s printed. After 
# calling the function, print both of your lists to make sure the messages were 
# moved correctly.

def send_messages(msg_list, sent_messages):
    # for msg in msg_list:
    #     sent_messages.append(msg)
    #     print(msg)
    while msg_list:
        msg = msg_list.pop()
        print(msg)
        sent_messages.append(msg)

msg_list = ['Hello world', 'I love Python', 'I hate Python']
sent_messages = []

send_messages(msg_list, sent_messages)

print(msg_list)
print(sent_messages)