#  8-4. Large Shirts: Modify the make_shirt() function so that shirts are large 
# by default with a message that reads I love Python. Make a large shirt and a 
# medium shirt with the default message, and a shirt of any size with a different 
# message.

def make_shirt(t_shirt_size='large', text='I love Python'):
    print(f"T_shirt size is {t_shirt_size} and following message is printed on the t_shirt:")
    print(f"{text}")

make_shirt()
make_shirt(t_shirt_size='medium')
make_shirt(t_shirt_size='small', text='I hate python')