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
        Bot_Response(message, ['selam', 'merhaba',],

                     'αℓєукϋмѕєℓαм'),

        Bot_Response(message, ['gittim', 'çıktım', 'kaçtım'], 
                     'sєlαmєtlє'),

        Bot_Response(message, ['iban', 'Iban'], '͏тovвεsтαүşıηηηηмм🤨'),

        Bot_Response(message, ['tanısalım mı', 'tanışalım', 'tanışabilirmiyiz',],
                     'σℓυя gєℓ çaу icєℓiм 🫖'),
        # new
        Bot_Response(message, ['nasılsın', 'neber',],
                     '𝐸𝓎𝓋𝒶𝓁𝓁𝒶𝒽'),
       
        Bot_Response(message, ['hello',],
             '𝒯ü𝓇𝓀ç𝑒 𝓀𝑜𝓃𝓊ş 𝒸𝒶𝓃ı𝓂🤗'),

        # Name
        Bot_Response(message, ['kimsin',],
                      '𝙂𝙚𝙫𝙚𝙯𝙚 𝙗𝙚𝙣'),
        # Help
        Bot_Response(message, ['fındık', 'fıstık', ],
                     'sєnsín fıstık 🥜'),
       
        # Website
        Bot_Response(message, ['bot', 'botmusun',], 
                      '𝒮𝑒𝓃𝓈𝒾𝓃 𝒷𝑜𝓉🤦'),
        
        #kare koyunca başına yazdıklarım geçersiz oluyor
        #ornek gösteriyorum
        # Bot_Response(message, ['botun cevap vereceği kelime',], 'botun yazacağı mesaj'),

        # Song
        Bot_Response(message, ['nerelisin',],
                     'sαnα nєrєsí lαzım'),
        # Notes
        Bot_Response(message, ['admin',],
                     'вuчur cαnım'),

        Bot_Response(message, ['günaydın',],
                     '☀️'),

        Bot_Response(message, ['geceler',],
                     '🌙'),

        # Nude Joke Lol
        Bot_Response(message, ['nude', 'nudes', ], 
                       'тovвεsтαүşıηηηηмм🤫'),

        # When Querry
        Bot_Response(message, ['aşkım', 'sevgilim',],
                     '❤️'),

        # When Website
        Bot_Response(message, ['muck', 'öpücük', 'öptüm',],
                     'вєncє öpmє αílє vαr😁'),

        # When Projects
        Bot_Response(message, ['ban'],
                      '🎈'),
      
         Bot_Response(message, ['küfür'],
                     'тєявιуєѕιzℓιкєтмє🤨'),
         
          Bot_Response(message, ['kes'],
                         '🤨🔪),     

          Bot_Response(message, ['sıkıldım'],
                       'ᔕıKı ᑕᗩᑎ IYIᗪIᖇ KOᒪᗩY çıKᗰᗩᘔ😂),     
 
 ]

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
