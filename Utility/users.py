import time

# class cmdUsers that stores every user that has used a command and the time of the last command and count of total commands used. Also stores blacklisted and whitelisted users.
class Users:
    def __init__(self):
        self.user_list = []
        self.blacklist = []
        self.whitelist = ['thelvl13mage']

    def add_user(self, username):
        self.user_list.append([username, time.time(), 1])

    def is_user_in_list(self, username):
        for user in self.user_list:
            if user[0] == username:
                return True
        return False

    def update_user_last_command(self, username):
        for user in self.user_list:
            if user[0] == username:
                user[1] = time.time()
                user[2] += 1

    def get_user_last_command_age(self, username):
        for user in self.user_list:
            if user[0] == username:
                return time.time() - user[1]

    def get_user_total_commands(self, username):
        for user in self.user_list:
            if user[0] == username:
                return user[2]

    def add_user_to_blacklist(self, username):
        self.blacklist.append(username)

    def add_user_to_whitelist(self, username):
        self.whitelist.append(username)

    def is_user_blacklisted(self, username):
        for user in self.blacklist:
            if user == username:
                return True
        return False

    def is_user_whitelisted(self, username):
        for user in self.whitelist:
            if user == username:
                return True
        return False

    def get_user_list(self):
        return self.user_list

    def get_blacklist(self):
        return self.blacklist

    def get_whitelist(self):
        return self.whitelist

    def remove_user_from_blacklist(self, username):
        for user in self.blacklist:
            if user == username:
                self.blacklist.remove(user)

    def remove_user_from_whitelist(self, username):
        for user in self.whitelist:
            if user == username:
                self.whitelist.remove(user)
    
    # get scoreboard with variable number of users
    def get_scoreboard(self, num_users):
        scoreboard = []
        for user in self.user_list:
            scoreboard.append([user[0], user[2]])
        scoreboard.sort(key=lambda x: x[1], reverse=True)
        return scoreboard[:num_users]
    
    # asynchronously persist users to file
    def persist_users(self, filename):
        with open(filename, 'w') as f:
            for user in self.user_list:
                f.write(f'{user[0]} {user[1]} {user[2]}\n')



    # asynchronously load users from file or create new file if it doesn't exist
    def load_users(self, filename):
        try:
            with open(filename, 'r') as f:
                for line in f:
                    line = line.strip()
                    line = line.split(' ')
                    self.user_list.append([line[0], float(line[1]), int(line[2])])
        except FileNotFoundError:
            with open(filename, 'w') as f:
                pass