#!/usr/bin/python3
""" Dictionary of list of dictionaries """

import json
import requests
import sys


def save_all_to_json():
    """ Expand on task 0 to export data in the JSON format """

    # Variables
    users_and_tasks = {}

    # Do GET requests
    users_json = requests.get(
        "https://jsonplaceholder.typicode.com/users/").json()
    todos_json = requests.get(
        "https://jsonplaceholder.typicode.com/todos").json()

    # Get the json from responses
    user_info = {}
    for user in users_json:
        user_info[user['id']] = user['username']

    for task in todos_json:
        if users_and_tasks.get(task['userId'], False) is False:
            users_and_tasks[task['userId']] = []
        task_dict = {}
        task_dict['username'] = user_info[task['userId']]
        task_dict['task'] = task['title']
        task_dict['completed'] = task['completed']
        users_and_tasks[task['userId']].append(task_dict)

    with open("todo_all_employees.json", "w") as jsonFile:
        json.dump(users_and_tasks, jsonFile)

if __name__ == "__main__":
    save_all_to_json()
