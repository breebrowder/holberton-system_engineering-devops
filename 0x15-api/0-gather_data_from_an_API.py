#!/usr/bin/python3
""" Gather data from an API """

import requests
import sys


def get_employee_tasks(employeeId):
    """ Get employee tasks """

    # Variables
    name = ''
    task_list = []
    completed_counter = 0

    # Do GET requests
    usersRes = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employeeId))
    todosRes = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".
        format(employeeId))

    # Get the json from responses
    name = usersRes.json().get('name')
    todosJson = todosRes.json()
    # Save the employee Name

    # Loop the tasks
    for task in todosJson:
        if task.get('completed') is True:
            completed_counter += 1
            # save the task title to task_list
            task_list.append(task.get('title'))

    # Print the first line
    print('Employee {} is done with tasks({}/{}):'.format(
        name, completed_counter, len(todosJson)))
    # Loop the task_list and print tasks
    for title in task_list:
        print('\t {}'.format(title))

    return 0

if __name__ == '__main__':
    get_employee_tasks(sys.argv[1])
