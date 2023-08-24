# Checks if the user's answer can be used by the determineReply() 
# function, and if it cannot provides an error.
def get_reply(user_input):
    if user_input.isdigit():
        user_input_int = int(user_input)
        return determine_reply(user_input_int)
    else:
        return 'Sorry, I don\'t understand your answer. I was looking for a number, not a string.'

# Determines the correct reply
def determine_reply(user_input_int):
    if user_input_int > 2:
        return 'Wow, that\'s a lot of coffee!'
    elif user_input_int == 0:
        return 'Should we go grab a coffee? I could use one too.'
    else:
        return 'Sounds like the right amount of coffee to start the day.'

# Determines the correct reply to the second question
def determine_second_reply(user_go_input):
    if user_go_input.lower() == 'yes':
        return 'Ok, let\'s go!'
    elif user_go_input.lower() == 'no':
        return 'Ok, see you later'
    else:
        return 'Sorry, I don\'t understand your answer. I need a yes or a no.'

reply = ''

while reply == '' or reply == 'Sorry, I don\'t understand your answer. I was looking for a number, not a string.':
    # Ask for user input
    user_coffee_input = input('How many cups of coffee have you had today? ')

    # Process the answer to get the right reply, and print that reply
    reply = get_reply(user_coffee_input)

    if reply == 'Should we go grab a coffee? I could use one too.':
        second_reply = ''
        while second_reply != 'Ok, let\'s go!' and second_reply != 'Ok, see you later':
            user_go_input = input(reply + ' ')
            second_reply = determine_second_reply(user_go_input)
            print(second_reply)
    else:
        print(reply)