# This file should contain a function called get_color_code().
# This function should take one argument, a color name,
# and it should return one argument, the hex code of the color,
# if that color exists in our data. If it does not exist, you should
# raise and handle an error that helps both you as a developer,
# for example by logging the request and error, and the user,
# letting them know that their color doesn't exist.
import json
import os


def get_color_code(color_name):
    # this is where you should add your logic to check the color.
    # Open the file at data/css-color-names.json, and return the hex code
    # The file can be considered as JSON format, or as a Python dictionary.
    a = "/Users/markusgarmeister/desktop/Foundation21/foundations-sample-website/color_check/data/css-color-names.json"
    color_list_path = open(a)
    color_dic = json.load(color_list_path)

    if color_name in color_dic.keys():
        return color_dic[color_name]

    else:
        return "Not a color!"
