#Lets you search the web
#Using either Google, Bing or Yahoo
#Written by Anupam

import webbrowser
engines = {"google": "www.google.com/searchq=", "bing": "www.bing.com/", "yahoo": "www.yahoo.com/"}

def search():
        if askEngine.lower() == "google":
                try:
                        webbrowser.open_new(engines["google"] + ask)
                except webbrowser.Error as e:
                        print(e)
        elif askEngine.lower() == "bing":
                try:
                        webbrowser.open_new(engines["bing"] + ask)
                except webbrowser.Error as e:
                        print(e)

        elif askEngine.lower() == "yahoo":
                try:
                        webbrowser.open_new(engines["yahoo"] + ask)
                except webbrowser.Error as e:
                        print(e)
        
while True:
        askEngine = input("Which engine would you like to use: ")
        if askEngine.lower() not in engines:
                print("Hey, hey! That search engine exists? Well, not for me.")
        else:
               ask = input("What would you like to search for: ")
               search()