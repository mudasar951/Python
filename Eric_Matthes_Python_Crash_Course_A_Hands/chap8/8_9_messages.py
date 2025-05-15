#  8-9. Messages: Make a list containing a series of short text messages. Pass the 
# list to a function called show_messages(), which prints each text message.

def show_messages(msg_list):
    for msg in msg_list:
        print(msg)

msg_list = ['Hello world', 'I love Python', 'I hate Python']

show_messages(msg_list)