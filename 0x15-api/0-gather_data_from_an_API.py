#!/usr/bin/python3

import requests
import sys

def get_employee_tasks(employeeId):
    # Variables
    name = ''
    task_list = []
    completed = 0

    # Perform GET requests
    userRes = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employeeId))
    todosRes = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(employeeId))

    print("userRes: {} \n".format(userRes))
    print("todosRes: {} \n".format(todosRes))
    # get JSON from responses
    name = userRes.json().get('name')
    print("Name: {}".format(name))

    todosJson = todosRes.json()
    # Save employee name

    # Loop tasks
    for task in todosJson:
        if task.get('completed') is True:
            completed += 1
            task_list.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(name, completed, len(todosJson)))
    for title in task_list:
        print("\t {}".format(title))

    return 0

if __name__ == "__main__":
    get_employee_tasks(sys.argv[1])
