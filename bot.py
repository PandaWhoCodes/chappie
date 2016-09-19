import telebot
import requests
import apiaiashish
bot=telebot.TeleBot("TELEGRAMBOTAPI")
print("started")


@bot.message_handler(commands=['start'])
def yoyo(message):
    x="Hi..!This is Chappie.\nWhat would you like to see today.\n\nThese are the aspects."
    x+="\nmovie\nmusic\nbooks\nauthors\nshows\ngame\n\nChoose any option and enter your choice in the format\n eg. movie : movie_name"

    bot.reply_to(message,x)
    #bot.reply_to(message,l)
def getResults(similarhtingi,context):
    query = similarhtingi.replace(' ', '+')
    url1 = 'https://www.tastekid.com/api/similar?q=' + query + '&k=TASTEKID KEY&format=json&type='+context
    r = requests.get(url1)
    x = eval(r.text)
    s="Suggestions based on your liking:\n"
    results=x["Similar"]["Results"]
    print(results)
    try:
        for i in range(4):
            s+=results[i]["Name"]+"\n"
    except:
        pass
    #s = '\n'.join([i["Name"] for i in x["Similar"]["Results"]])
    #print(s)
    if len(s)<1:
        return "Sorry coudn't Find anything. Try somethig else"
    return s

@bot.message_handler(func=lambda message:True)
def mainfunction(message):
    context=""
    json_obj=api.main(message.text)
    if len(json_obj["result"]["parameters"])>0:
        if "MovieWant" in json_obj["result"]["parameters"]:
            context="movie"
        elif "MusicWant" in json_obj["result"]["parameters"]:
            context="music"
        elif "BooksWant" in json_obj["result"]["parameters"]:
            context="books"
        elif "GameWant" in json_obj["result"]["parameters"]:
            context="game"
    if context=="movie":
        try:
            if len(json_obj["result"]["parameters"]["movie"])>0:
                themovie=json_obj["result"]["parameters"]["movie"]
                bot.reply_to(message, getResults(themovie,context))
                return
        except:
            pass
    elif context=="music":
        try:
            if len(json_obj["result"]["parameters"]["music"])>0:
                themovie=json_obj["result"]["parameters"]["music"]
                bot.reply_to(message, getResults(themovie,context))
                return
        except:
            pass

    print(str(json_obj))
    try:
        bot.reply_to(message,json_obj["result"]["fulfillment"]["speech"])
    except:
        bot.reply_to(message,"Sorry. Try something else :(")


bot.polling()
