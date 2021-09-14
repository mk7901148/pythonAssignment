import json
from difflib import get_close_matches



def readFileToListData():
    txt_file = open("list.txt", "r")
    file_content = txt_file.read()
    #print("The file content are: ", file_content)

    content_list = file_content.split("\n")
    txt_file.close()
    return content_list
    print("The list is: ", content_list)


def SearchListEngine(searchWord):
    data = readFileToListData()
    searchWord = searchWord.lower()
    if searchWord in data:
        return searchWord
    elif len(get_close_matches(searchWord, data)) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(searchWord, data)[0])
        if yn == "Y":
            return get_close_matches(searchWord, data)[0]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")
output = SearchListEngine(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)