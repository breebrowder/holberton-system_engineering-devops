#!/usr/bin/python3
""" Export to JSON """

import json
import requests
import sys


def save_tasks_to_json(employeeId):
    """ Expand on task 1 to export data in the JSON format """

    # Variables
    username = ''
    userDict = {}

    # Do GET requests
    usersRes = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employeeId))
    todosRes = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".
        format(employeeId))

    # Get the json from responses
    username = usersRes.json().get('username')
    todosJson = todosRes.json()
    # Save the employee Name

    userDict[employeeId] = []

    # Loop through and save
    for task in todosJson:
        taskDict = {}
        taskDict['task'] = task.get('title')
        taskDict['username'] = username
        taskDict['completed'] = task.get('completed')

        userDict[employeeId].append(taskDict)

        with open("{}.json".format(employeeId), "w") as jsonFile:
            json.dump(userDict, jsonFile)

if __name__ == "__main__":
    save_tasks_to_json(sys.argv[1])
