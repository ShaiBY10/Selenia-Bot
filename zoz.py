import github
import random

# "log in proccess with github token (https://github.com/settings/tokens)
g = github.Github("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").get_user()
# getting the repository
repo = g.get_repo("Selenia-Bot")
# getting a list of all items in {Selenia-bot} repo
pics = repo.get_contents("pics")
number_of_pics = len(pics)

# setting the link to be a list so i can change a char in a specific index
# index 64 is the index that i need to change for the RNG to work
link = list("https://github.com/ShaiBY10/Selenia-Bot/blob/master/pics/zoz%20(1).jpeg")


# define a function that takes the link and changes index 64 to be a random number from 1 to the length of the "pics"
# folder in my github repo.
def link_generator(link):
    link[64] = random.randint(1, number_of_pics)
    print(*link,sep="")




