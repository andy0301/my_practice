#!/usr/local/bin/python3

# Assume there is a REST API available at "http://www.linkedin.corp/api" for accessing employee information. The employee information endpoint is "/employee/<id>". 
# Each employee record you retrieve will be a JSON object with the following keys:
#
#   - 'name'  refers to a String that contains the employee's first and last name
#
#   - 'title' refers to a String that contains the employee's job title
#
#   - 'reports' refers to an Array of Strings containing the IDs of the employee's direct reports
#
#
# Sample JSON API Response.
# Sample JSON
# # GET /employee/A123456789
# {
#  "name": "Flynn Mackie",
#  "title": "Senior VP of Engineering",
#  "reports": ["A123456793", "A1234567898"]
# }
#
# Write a function that will take an employee ID and print out the entire hierarchy of employees under that employee.
#
# For example, suppose that Flynn Mackie's employee id is 'A123456789' and his only direct reports are Wesley Thomas and Nina Chiswick. 
# If you provide 'A123456789' as input to your function, you will see the sample output below.
#
#
#
# -----------Begin Sample Output--------------
# Flynn Mackie - Senior VP of Engineering
#   Wesley Thomas - VP of Design
#     Randall Cosmo - Director of Design
#       Brenda Plager - Senior Designer
#   Nina Chiswick - VP of Engineering
#     Tommy Quinn - Director of Engineering
#       Jake Farmer - Frontend Manager
#         Liam Freeman - Junior Software Engineer
#       Sheila Dunbar - Backend Manager
#         Peter Young - Senior Code Cowboy
#
# -----------End Sample Output--------------

# AWB NOTE: I switched to bash here
# mostly because I'm more comfortable using curl and I didn't know off-hand
# whether I could use google to determine which library to include
# in order to make http requests - turns out it is "requests"
# FYI: I struggled a little bit with vim mode in the coderpad... it isn't
# completely vi-like. For example, you can't hold down the "k" key to 
# move upwards

# During the test, the run button is disabled, so you can't actually
# test anything. This doesn't really jive with how I code
# Let’s say I had to build a binary tree to store integers.
# Literally, my first step would be to write a loop that prints out
# each of the integers in the list. I would run that to make sure it
# works, THEN I would add a function to print the tree (the tree
# that doesn’t exist yet), then I would write the insert statement
# with lots of debugging statements so I can see what it is doing to
# test my logic

# mock function because the rest api doesn't actually exist

# create a mock api call using requests module

import requests
import json

def mockApiCall(empId):
    
    if result.status_code == 200:
         # return mock results json file
        if empId == "A123456789":
            svp = {"name": "Flynn Mackie","title": "Senior VP of Engineering","reports": ["A123456793", "A1234567898"]}
            return (json.dumps(svp))
        elif empId == "A123456793":
            vp1 = {"name":"Wesley Thomas","title":"VP of Design","reports": ["A1234567931"]}
            return (json.dumps(vp1))
        elif empId == "A1234567898":
            vp2 = {"name":"Nina Chiswick","title":"VP of Design","reports": ["A1234567933"]}
            return (json.dumps(vp2))
        elif empId == "A1234567931":
            d1 = {"name":"Randall Cosmo", "title":"Director of Design" ,"reports": []}
            return(json.dumps(d1))
        elif empId == "A1234567933":
            d2 = {"name":"Tommy Quinn","title":"Director of Engineering","reports": ["A12345678981"]}
            return (json.dumps(d2))
        elif empId == "A12345678981":
            fm = {"name":"Jake Farmer","title":"Frontend Manager","reports": []}
            return (json.dumps(fm))
    else:
        return ("Api call failed with error status {}".format(result.status_code))



   
if __name__ == "__main__":
    getEmpInfo('A123456789')