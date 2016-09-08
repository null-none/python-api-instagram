import requests


class instagramAPI(object):

    def __init__(self, access_token):
        self.url = 'https://api.instagram.com/v1'
        self.access_token = access_token

    def users_self(self):
        r = requests.get('{0}/users/self/?access_token={1}'.format(self.url, self.access_token))
        return r.text

    def users_detail(self, user_id):
        r = requests.get('{0}/users/{1}/?access_token={2}'.format(self.url, user_id, self.access_token))
        return r.text

    def users_self_media_liked(self):
        r = requests.get('{0}/users/self/media/liked?access_token={1}'.format(self.url, self.access_token))
        return r.text

    def followed_by(self):
        r = requests.get('{0}/users/self/followed-by?access_token={1}'.format(self.url, self.access_token))
        return r.text

    def follows_self(self):
        r = requests.get('{0}/users/self/follows?access_token={1}'.format(self.url, self.access_token))
        return r.text

    def media(self, media_id):
        r = requests.get('{0}/media/{1}?access_token={2}'.format(self.url, media_id, self.access_token))
        return r.text

    def media_self_recent(self):
        r = requests.get('{0}/users/self/media/recent?access_token={1}'.format(self.url, self.access_token))
        return r.text
