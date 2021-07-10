title = "Python JokeBot"
print(title.upper())
number = int(input("What's your favourite number? 1-100: "))
if number < 25:
    Joke = "Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them."
elif number < 50:
    Joke = "Why do we tell actors to 'break a leg?' Because every play has a cast!"
elif number < 75:
    Joke = "Helvetica and Times New Roman walk into a bar. 'Get out of here!' shouts the bartender. 'We don’t serve your type.'"
elif number < 101:
    Joke = "Hear about the new restaurant called Karma? There’s no menu: You get what you deserve."
print(Joke)