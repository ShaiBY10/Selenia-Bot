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

example = "https://github.com/ShaiBY10/Selenia-Bot/blob/master/pics/zoz%20(1).jpeg?raw=true"


# convert the example string into a list
# replace the list index 64 with a random number in range of the len of pics
def generate(link):
    listed = list(link)
    listed[64] = str(random.randint(1, len(pics)))  # str method to prevent Type Error
    return listed


def list_string(li):
    new_str = ""
    return new_str.join(li)



