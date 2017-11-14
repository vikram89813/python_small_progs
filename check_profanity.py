import urllib

def read_text():
    quotes = open("/Users/kumarvikram/codes/udacity_python/movie_quotes.txt")
    contents = quotes.read()
    print (contents)
    quotes.close()
    check_profanity(contents)

def check_profanity(to_check):
    connection=urllib.urlopen(" http://www.wdylike.appspot.com/?q="+to_check)
    output=connection.read()
    print(output)
    connection.close()

read_text()