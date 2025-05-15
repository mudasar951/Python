# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the 
# function send_messages() with a copy of the list of messages. After calling the 
# function, print both of your lists to show that the original list has retained its 
# messages.

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

send_messages(msg_list[:], sent_messages)

print(msg_list)
print(sent_messages)