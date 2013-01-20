import pylast
from ApiKeys import *

class LastFm():
    def __init__(self, username):
        self.network = pylast.LastFMNetwork(api_key = ApiKeys.api_key, api_secret = ApiKeys.api_secret)
        self.user = username

    def get_username(self):
        return self.network.get_user(self.user).get_name()

    def get_number_scrobblings(self):
        return self.network.get_user(self.user).get_playcount()

    # Returns 'number' top weekly artist from last fm (position, name, number_of_scrobblings)
    def get_week_artist(self, number):
        self.all_artist = self.network.get_user(self.user).get_top_artists(pylast.PERIOD_7DAYS)
        self.result = []

        for artist in range(0,number):
            self.result.append((artist,self.all_artist[artist].item.get_name(),self.all_artist[artist].weight))

        return self.result
