import re


def Bot_Response(message, response_array, response):
    # Splits the message and the punctuation into an array
    list_message = re.findall(r"[\w']+|[.,!?;]", message.lower())

    # Scores the amount of words in the message
    score = 0
    for word in list_message:
        if word in response_array:
            score = score + 1

    # Returns the response and the score of the response
    # print(score, response)
    return [score, response]


def get_response(message):
    # Add your custom responses here
    response_list = [
        Bot_Response(message, ['selam', 'merhaba', 'hello',],

                     'Aleykümselam'),

        Bot_Response(message, ['gittim', 'çıktım', 'kaçtım'], 
                     'selametle'),

        Bot_Response(message, ['cmd', 'type cmd'], 'click me /list'),

        Bot_Response(message, ['kurucu'],
                     '@Cengonuzz'),
        # new
        Bot_Response(message, ['nasılsın', 'neber',],
                     'eyvallah'),

        # Name
        Bot_Response(message, ['kimsin', 'tanışalım', 'tanışabilirmiyiz',],
                      'gevezeben'),
        # Help
        Bot_Response(message, ['ta],
                     'I will do my best to assist you!'),
        # Website
        Bot_Response(message, ['link', 'links',], 
                      '@vefaasohbet'),

        # Song
        Bot_Response(message, ['nerelisin',],
                     'sana neresi lazım '),

        # Notes
        Bot_Response(message, ['admin',],
                     'buyur canım '),

        Bot_Response(message, ['günaydın',],
                     '☀️'),

        Bot_Response(message, ['iyi geceler',],
                     '🌙'),

        # Nude Joke Lol
        Bot_Response(message, [
                     'nude', 'nudes', ], '🤫'),

        # When Querry
        Bot_Response(message, ['aşkım', 'sevgilim',]
                     'developer'], '❤️'),

        # When Website
        Bot_Response(message, ['website', 'amrohan', 'web', 'developer'],
                     'https://www.rohan.ml'),

        # When Projects
        Bot_Response(message, ['projects', 'project', 'proj','pro','projec', 'proje'],
                     'Here you Go\n /projects'),



    # Checks all of the response scores and returns the best matching response
    response_scores = []
    for response in response_list:
        response_scores.append(response[0])

    # Get the max value for the best response and store it into a variable
    winning_response = max(response_scores)
    matching_response = response_list[response_scores.index(winning_response)]

    # Return the matching response to the user
    if winning_response == 0:
        score = score + 1
    else:
        bot_response = matching_response[1]

    print('Bot response:', bot_response)
    return bot_response
