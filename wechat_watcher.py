import re
from wxpy import *

class WeChat_Watcher():
    def __init__(self, group_name, user_name, watch_function):
        self.bot = Bot(True)
        self.bot.groups(update=True, contact_only=False)
        self.group = self.get_group(group_name)
        self.user = self.get_group_user(self.group, user_name)
        self.watch_function = watch_function

    def get_group(self, group_name):
        bot = self.bot
        return ensure_one(bot.groups().search(group_name))

    def get_user(self, username):
        bot = self.bot
        return ensure_one(bot.friends().search(username))

    def get_group_user(self, group, username):
        return group.search(username)

    def watch_all_group(self,watch_function):
        bot = self.bot

        # watch group user's message and process it
        @bot.register(Group, TEXT, except_self=False)
        def watch_all_group_msg(msg):
            if watch_function is not None:
                watch_function(msg)
        # embed()

    def watch_group(self, group, user, watch_function):
        bot = self.bot

        @bot.register(group, TEXT, except_self=False)
        def watch_group_msg(msg):
            if watch_function is not None:
                watch_function(msg)
        # embed()

    def watch_group_user(self, group, user, watch_function):
        bot = self.bot

        # watch group user's message and process it
        @bot.register([group, user], TEXT, except_self=False)
        def watch_group_user_msg(msg):
            if watch_function is not None:
                watch_function(msg)
        # embed()
