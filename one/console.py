#!/usr/bin/python3

import cmd
import json
import re
import sys

import models
from models import storage as my_storage


class MyCommand(cmd.Cmd):
    prompt = "(my_prompt) "

    def do_EOF(self, *args):
        '''Exits the program'''
        print()
        return True

    def do_exit(self, *args):
        '''Exits the program'''
        return True

    def do_create(self, line):
        '''Creates an instance of the specified class'''
        if line:
            if line not in my_storage.classes():
                print("** Class doesn't exist **")
            else:
                new_instance = my_storage.classes()[line]()
                new_instance.save()
                print(new_instance.id)
        else:
            print("** Class name is missing **")

    # Other methods (do_show, do_destroy, do_all, do_update, emptyline, precmd, do_count)

if _name_ == '_main_':
    MyCommand().cmdloop()
