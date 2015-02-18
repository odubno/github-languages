#importing some dependencies for this program
import sys
import operator
from collections import defaultdict

import requests


#this function takes a GitHub username as an argument and returns their info
def get_repositories(user):
	"""Retrieves a list of user's repositories"""

	
	url = "https://api.github.com/users/{user}/repos".format(user=user)
	response = requests.get(url) #GET the request to the endpoint
	return response.json() #parse the JSON and return it as a Python list

def main():
	""" Main function """

#calls gets_repositoreis function
#passing first command line argument
	repositories = get_repositories(sys.argv[1]) 
	print repositories

#calling the main function from the main block of the script
if __name__ == "__main__":
    main()
