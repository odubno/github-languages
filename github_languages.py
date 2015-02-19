import sys
import operator
from collections import defaultdict
from secret import USERNAME, PASSWORD

import requests


#this function takes a GitHub username as an argument and returns their info
def get_repositories(user):
    """ Retreive a list of a user's repositories """
    url = "https://api.github.com/users/{user}/repos".format(user=user)
    #GET the request to the endpoint
    response = requests.get(url, auth=(USERNAME, PASSWORD))
    #parse the JSON and return it as a Python list
    return response.json()

def get_language_dictionaries(repositories):
    """
    Return a list of dictionaries containing the languages used in each
    repository
    """
    language_dictionaries = []
    for repository in repositories:
        url = "https://api.github.com/repos/{owner}/{repo}/languages"
        url = url.format(owner=repository["owner"]["login"],
                         repo=repository["name"])
        response = requests.get(url, auth=(USERNAME, PASSWORD))
        language_dictionaries.append(response.json())
    return language_dictionaries

def accumulate_languages(language_dictionaries):
    """ Calculate the total data size for each language """
    accumulated = defaultdict(int)
    total = 0
    for language_dictionary in language_dictionaries:
        for language_name, number_of_bytes in language_dictionary.iteritems():
            accumulated[language_name] += number_of_bytes
            total += number_of_bytes
    return accumulated, total


def main():
    """ Main function """

    #calls gets_repositoreis function
	#passing first command line argument
    repositories = get_repositories(sys.argv[1])
    language_dictionaries = get_language_dictionaries(repositories)
    language_totals, total_bytes = accumulate_languages(language_dictionaries)

    sorted_language_totals = sorted(language_totals.iteritems(),key=operator.itemgetter(1),reverse=True)

    for language_name, number_of_bytes in sorted_language_totals:
        percentage = 100.0 * number_of_bytes / total_bytes
        print "{}: {:.2f}%".format(language_name, percentage)

    print language_dictionaries


#calling the main function from the main block of the script
if __name__ == "__main__":
    main()

#Main is used as an entry point in programming. When you run a program the first thing that runs is main
#Where all the interaction takes place


