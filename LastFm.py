import pylast
from ApiKeys import *

class LastFm():
    def __init__(self, username):
        self.network = pylast.LastFMNetwork(api_key = ApiKeys.api_key, api_secret = ApiKeys.api_secret)
        self.user = username

    def get_username(self):
        return self.network.get_user(self.user).get_name()
