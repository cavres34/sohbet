import re

def Bot_Response(message, response_array, response):

    # Splits the message and the punctuation into an array

    


    # Add your custom responses here

    response_list = [

        Bot_Response(message, ['sa', 'sea', 'slm', 'merhaba', 'selam'],

                     'Ve aleyküm selam merhaba bebeğim'),

        Bot_Response(message, ['by', 'bb', 'gidiyorum', 'gittim'], 'Görüşürüz yigidim😘'),

        Bot_Response(message, ['naber', 'nbr'], 'iyidir yavrum senden naber'),

        Bot_Response(message, ['nasılsın'],

                     'Sen sorunca canom iyiyim iyiyim'),

        # new

        Bot_Response(message, ['how', 'you', 'created'],

                     'I was created by using python and got deployed on Herkou'),

        # Name

        Bot_Response(message, ['your', 'name'],

                     'My name is Rohan\'s Bot, nice to meet you!'),

        # Help

        Bot_Response(message, ['help', 'please'],

                     'I will do my best to assist you!'),

        # Website

        Bot_Response(message, ['link', 'links', ], 'website https://rohan.ml'),

        # Song

        Bot_Response(message, ['play', 'song', ],

                     'https://youtu.be/edzt82nC45k'),

        # Notes

        Bot_Response(message, ['notes', 'note', ],

                     'Soon, notes will be available'),

        Bot_Response(message, ['socials', 'socials', ],

                     'Here you Go\n /socials'),

        Bot_Response(message, ['source', 'code', ],

                     'Here you Go\n /source_code'),

        # Nude Joke Lol

        Bot_Response(message, [

                     'nude', 'nudes', ], 'I just took a screenshot, and I\'m sending your photo to @amrohan right now, you lil horny ass😏'),

        # When Querry

        Bot_Response(message, ['when', '?', 'query', 'question', 'inform',

                     'developer'], 'Inquire with the developer about this. @amrohan'),

        # When Website

        Bot_Response(message, ['website', 'amrohan', 'web', 'developer'],

                     'https://www.rohan.ml'),

        # When Projects

        Bot_Response(message, ['projects', 'project', 'proj','pro','projec', 'proje'],

                     'Here you Go\n /projects'),

    ]

    # Checks all of the response scores and returns the best matching response


   

    print('Bot response:', bot_response)

    return bot_response
