import github
import random
import os

# "log in proccess with github token (https://github.com/settings/tokens)
GIT_TOKEN = os.environ.get("GIT_TOKEN")
g = github.Github(GIT_TOKEN).get_user()
# getting the repository
repo = g.get_repo("Selenia-Bot")
# getting a list of all items in {Selenia-bot} repo
pics = repo.get_contents("pics")
number_of_pics = len(pics)

example = "https://github.com/ShaiBY10/Selenia-Bot/blob/master/pics/zoz%20(1).jpeg"


# convert the example string into a list
# replace the list index 64 with a random number in range of the len of pics
def generate(link):
    new = list(link)
    new[64] = str(random.randint(1, len(pics)))  # str method here to prevent type error
    return new


# convert the list into string again
def list_to_string(li):
    converted = ""
    return converted.join(li)


unconverted_link = generate(example)
pic = list_to_string(unconverted_link)
