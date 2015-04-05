#!/usr/bin/env python
# encoding: utf-8
"""
BanyanParser.py
Created by Robert Dempsey on 1/23/15.
Copyright (c) 2015 Robert Dempsey. All rights reserved.

Taken from Banyan: https://github.com/rdempsey/banyan
"""

from pyparsing import *
from bin.LocalFile import *
from bin.Mailer import *
from bin.WebSearch import *
from bin.LocalProject import *

lower = str.lower


class BanyanParser:
    def __init__(self, **kwargs):
        self.properties = kwargs

    # Input
    @property
    def input(self):
        return self.properties.get('input', 'None')

    @input.setter
    def input(self, s):
        self.properties['input'] = s

    @input.deleter
    def input(self):
        del self.properties['input']

    def parse(self):
        """
        Commands
        word            ::      group of alphabetic characters
        command         ::      the first word of the sentence
        command_object  ::      what the command needs to do

        Questions
        question        ::      the first word of the sentence begins with a contraction
        """

        # Put the input into a string
        input = self.input

        # Parse Actions
        join_tokens = lambda tokens : " ".join(tokens)

        # Define grammar
        comma = Literal(",").suppress()
        command = oneOf("check Check create Create open Open search Search get Get email Email tweet Tweet")
        act_on = oneOf("project file web locally")
        command_object = OneOrMore(Word(alphas+"'."))
        what_time = oneOf("current today's tomorrow's")
        subject = Literal("subject")

        # Assign parse actions
        command_object.setParseAction(join_tokens)

        # Commands
        create_open_search = command("command") + act_on("act_on") + command_object("name")
        get = command("command") + what_time("time") + command_object("object")
        email = command("command") + command_object("email_to") + comma + subject + command_object("email_subject")
        tweet = command("command") + command_object("tweet")
        launch_check = command("command") + command_object("app")

        try:
            w = command.parseString(input)
            w_command = lower(w[0])
            if w_command == "create":
                c = create_open_search.parseString(input)
                if c.act_on == "project":
                    system("say Shall I store the project in a private repo?")
                    save_in_github = raw_input("Save in Github > ")
                    p = LocalProject()
                    p.create_new_project(c.name, save_in_github)
                elif c.act_on == "file":
                    #TODO: add create file
                    pass
            elif w_command == "check":
                chk = launch_check.parseString(input)
                if chk.app == "email":
                    SayGmailCount().start()
                    SayADSCount().start()
                    SayDC2Count().start()
            elif w_command == "open":
                c = create_open_search.parseString(input)
                if c.act_on == "file":
                    f = LocalFile()
                    f.open_file(c.name)
                elif c.act_on == "project":
                    #TODO: add open project
                    pass
                else:
                    pass
            elif w_command == "search":
                s = create_open_search.parseString(input)
                if s.act_on == "web":
                    ws = WebSearch()
                    ws.perform_search(s.name)
            elif w_command == "email":
                e = email.parseString(input)
                print("email: {}, subject: {}".format(e.email_to, e.email_subject))
            elif w_command == "tweet":
                #TODO: add tweeting
                # t = tweet.parseString(input)
                pass
            else:
                print("I don't know what you want me to do...")
        except Exception as e:
            system("say Please enter a valid command")
            print("Error: {}".format(str(e)))



if __name__ == '__main__':
    pass