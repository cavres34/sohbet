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

        Bot_Response(message, ['çıktım', 'kaçtım'], 
                     'sєlαmєtlє'),
          

        Bot_Response(message, ['rica',],
             'nє kαdαr kíbαrsın sєn öчlє🤗'),   
      
        Bot_Response(message, ['iban', 'Iban'], '͏тovвεsтαүşıηηηηмм🤨'),

        Bot_Response(message, ['tanısalım mı', 'tanışalım', 'tanışabilirmiyiz',],
                     'σℓυя gєℓ çaу icєℓiм 🫖'),
        # new
        Bot_Response(message, ['nasılsın', 'neber',],
                     '𝐸yvallah'),
       
        Bot_Response(message, ['naber',] , 'iyi senden'),


       Bot_Response(message, ['aşk',],
                     'ne gereksiz😒'),
       
       Bot_Response(message, ['orta', 'sade', 'şekerli',],
                     'az yede kendine hizmetçi tut😁'),   


        Bot_Response(message, ['pm', 'dm', 'özel',],
                     'blader yasak yasak'),
      
        Bot_Response(message, ['hello',],
             'türkçe konuş canım 😁'),
             
        Bot_Response(message, ['tamam',], 'sen tamam diyorsan tamamdır'), 
        
        Bot_Response(message, ['öyle',], 
           'öyle diyorsan öyledir'), 
      
        Bot_Response(message, ['neden',], '𝐻𝑒𝓇 𝒮̧𝑒𝓎𝒾𝓃 𝐵𝒾𝓇 𝒩𝑒𝒹𝑒𝓃𝒾 𝒱𝒶𝓇𝒹ı𝓇'), 
       
        # Name
        Bot_Response(message, ['kimsin',],
                      '𝙂𝙚𝙫𝙚𝙯𝙚 𝙗𝙚𝙣'),
        # Help
        Bot_Response(message, ['fındık', 'fıstık', ],
                     'sєnsín fıstık 🥜'),
   
        Bot_Response(message, ['kahve', ],
                     'nasıl içersin gülüm'),    
      
        # Website
        Bot_Response(message, ['bot', 'botmusun',], 
                      'Sensin bot🤦'),
        
        #kare koyunca başına yazdıklarım geçersiz oluyor
        #ornek gösteriyorum
        # Bot_Response(message, ['botun cevap vereceği kelime',], 'botun yazacağı mesaj'),

        # Song
        Bot_Response(message, ['nerelisin',],
                     'sαnα nєrєsí lαzım'),
        # Notes
        Bot_Response(message, ['admin',],
                     'вuчur cαnım'),

        Bot_Response(message, ['çay',],
                     'hüseyin işi bıraktı😁'),
      
        Bot_Response(message, ['günaydın',],
                     'Günüm şimdi aydı güzel insan☀️'),

        Bot_Response(message, ['geceler',],
                     'İyi geceler Benli rüyalar 😂🌙'),

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
                      'İşte biri daha uçtu🎈'),
      
         Bot_Response(message, ['küfür'],
                     'тєявιуєѕιzℓιкєтмє🤨'),
         
          Bot_Response(message, ['kes'],
                         '🤨🔪'),     
 
          Bot_Response(message, ['gider'],
                        'senin yaptığın gider ancak benim hoşuma gider😝'),     
         
          Bot_Response(message, ['ayıp',],
                     'ayıpın yolları kayıp😅'),

          Bot_Response(message, ['sıkıldım'],
                       'ᔕıKı ᑕᗩᑎ IYIᗪIᖇ KOᒪᗩY çıKᗰᗩᘔ😂'),     

           Bot_Response(message, ['sus'],
                        'nєdєnmíş вєn kσnuşmαk íçín чαpıldım🤨'),
          
           Bot_Response(message, ['trip'],
                       'Hayda ben naptım be şimdi🫣'),
 
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
