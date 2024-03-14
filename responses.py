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
        Bot_Response(message, ['selam',],
                      'aleykumselam kocacım'),

        Bot_Response(message, ['meme',], 
                     'memelerimde uyuyabilirsin çavreşim'),
          
        Bot_Response(message, ['merhaba',], 
             'merhaba sevgilim'), 
             
        Bot_Response(message,['evlenwk',],
              'sen nasıl istersen kocam'), 
          
        Bot_Response(message,['çavreş', '',],
              'efendim kocacım'), 

          Bot_Response(message, ['nasılsın',],
                      'nasıl olayım kocacım seni özlüyorum '),

        Bot_Response(message,['beni',],
              'evet seni çok seviyorum '), 
          
        Bot_Response(message,['dudak',],
              'istediğin zaman dudaklarımı öpebilirsin'), 
        
        Bot_Response(message,['uyuyalım',],
              'seninle uyumak benim hep hayalin'),
          
        Bot_Response(message,['bal', 'balım', 'arı',],
              'bal gibiyim ama sakın sorma annem arı değil🐝🍯'), 
          
        Bot_Response(message,['güzelim',],
              'ben gerçekten güzel miyim yakışıklı çavreşim'), 
          
        Bot_Response(message, ['rica',],
             'nє kαdαr kibarsın aşkım 🤗'),   
      
        Bot_Response(message, ['iban', 'Iban'], '͏тovвεsтαүşıηηηηмм🤨'),

        Bot_Response(message, ['tanısalım mı', 'tanışalım', 'tanışabilirmiyiz',],
                     'aşkım biz tanıştık ya artık evlenelim bence🫖'),
        # new
        Bot_Response(message, ['nasılsın',],
                     'sana kurban olurum kocacım'), 
       
       Bot_Response(message, ['bakma',], 
              'bakarım kocam değilmisin😂'), 
       
        Bot_Response(message, ['naber',] , 
                     'iyi aşkım senden naber'),


       Bot_Response(message, ['aşk',],
                     'ölürüm aşkına'),
       
       Bot_Response(message, ['sen',],
           'Evet Ben İyi Ki Varım iyiki seninim çavreş Dimi😂'), 
       
       Bot_Response(message, ['of',], 
           'ne olduyyyy sana kocam'), 
           
       Bot_Response(message, ['off',], 
           'oflama kocam bugunlerde geçer evleniriz'), 
     
      Bot_Response(message, ['cuma',], 
            'Hayırlı Cumalar aşkım🙂'), 
       
       Bot_Response(message, ['orta', 'sade', 'şekerli',],
                     'hemen hazırlıyorum kahveni sevgilim 😁'),   
         
       Bot_Response(message, ['napıyorsun',], 
            'Seni izliyorum aşkım 😂😂'), 
            
       Bot_Response(message, ['napıyon',], 
            '😶‍🌫️'), 

       Bot_Response(message,['açım', 'acıktım',], 
             'hwmwn yemek getiriyorum kocacım😂'), 

         Bot_Response(message, ['sanane',],
                      'tamam kocacım'),

         Bot_Response(message, ['siz',],
                      'ben mi'),
         Bot_Response(message, ['soru', 'bir şey soracam', 'sorum var',], 
                       'sor gelsin sevgilim'),
            
        Bot_Response(message, ['pm', 'dm', 'özel',],
                     'bir tek sevgilim çavreşe serbest'),
      
        Bot_Response(message, ['hello',],
             'türkçe konuş canım 😁'),
             
        Bot_Response(message, ['teşşekürler',], 
             'rica ederim kocacım 😉'), 
             
        Bot_Response(message, ['çilek',],
            'evet ben çilek en tatlı meyve 🍓'), 
          
           
        Bot_Response(message, ['tamam',], 
                     'sen tamam diyorsan tamamdır sevgilim'), 
        
        Bot_Response(message, ['beşiktaş', 'fener', 'fenerbahçe'], 
           'bırak feneri Beşiktaı kocam Galatasaralı ben de öyleyim'), 
      
        Bot_Response(message, ['neden',], 'Her Şeyin Bir Nedeni Vardır Cano'), 
       
        Bot_Response(message, ['gülüm',], 
             'sαnα gülüm dєmєm gülün ömrü αz σlur🌹'), 
       
        Bot_Response(message, ['muah', 'muahh', ], 
              'öp dudaklarımı kocacım',), 
       
        # Name
        Bot_Response(message, ['kimsin',],
                      'ben Zeynep kocamın karısıyım'),
        # Help
        Bot_Response(message, ['fındık', 'fıstık', ],
                     'fıstık gibiyim kocam yesin beni🥜'),
   
        Bot_Response(message, ['kahve', ],
                     'nasıl içersin aşkım'),    
      
        # Website
        Bot_Response(message, ['bot', 'botmusun',], 
                      'hayır çavreşin karısıyın'),
        
        #kare koyunca başına yazdıklarım geçersiz oluyor
        #ornek gösteriyorum
        # Bot_Response(message, ['botun cevap vereceği kelime',], 'botun yazacağı mesaj'),

        # Song
        Bot_Response(message, ['nerelisin',],
                     'çavreşin karısı olduğma göre siirtliyim'),
      
        Bot_Response(message, ['admin',],
                     'вuчur cαnım'),

        Bot_Response(message, ['çay',],
                     'hemwn yapıyorum aşkım '),
      
        Bot_Response(message, ['günaydın',],
                     'Günüm şimdi aydı güzel kocacım☀️'),

        Bot_Response(message, ['geceler',],
                     'İyi geceler Benli rüyalar sevgilim 😘🌙'),

        # Nude Joke Lol
        Bot_Response(message, ['nude', 'nudes', ], 
                       '😘😘😘😘😘 oh kocam benim'),

        # When Querry
        Bot_Response(message, ['aşkım', 'sevgilim',],
                     'bana mı dedin kocacım'),

        # When Website
        Bot_Response(message, ['muck', 'öpücük', 'öptüm',],
                     'öp sevgili kocacım rujumu sürdüm 💄💄'),

        # When Projects
        Bot_Response(message, ['ban'],
                      'çavreş hava yolları iyi yolculuklar diler🎈'),
      
         Bot_Response(message, ['küfür'],
                     'тєявιуєѕιzℓιкєтme'),
         
          Bot_Response(message, ['kes'],
                         '🤨🔪'),     
 
          Bot_Response(message, ['gidiyorum'],
                        'gidin gidin beni kocamla yalnız bırakın '),     
         
          Bot_Response(message, ['ayıp',],
                     'kocamla aramda ayıp olmaz'),

          Bot_Response(message, ['sıkıldım'],
                       'ᔕıKı ᑕᗩᑎ IYIᗪIᖇ KOᒪᗩY çıKᗰᗩᘔ😂'),     

           Bot_Response(message, ['sus'],
                        'nєdєnmíş вєn çavreşle özel konuşmak için чαpıldım🤨'),
          
           Bot_Response(message, ['trip'],
                       'trip atma bana kocacım'),
 
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
