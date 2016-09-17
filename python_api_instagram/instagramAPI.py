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

    def actions_relationship(self, user_id, action):
        data = {
            'access_token': self.access_token,
            'action': action
        }
        r = requests.post('{0}/users/{1}/relationship?access_token={2}'.format(self.url, user_id, self.access_token), data=data)
        return r.text

    def relationship(self, user_id):
        r = requests.get('{0}/users/{1}/relationship?access_token={2}&action={3}'.format(self.url, user_id, self.access_token))
        return r.text

    def requested_by(self):
        r = requests.get('{0}/users/{1}/users/self/requested-by?access_token={1}'.format(self.url, self.access_token))
        return r.text

    def followed_by(self):
        r = requests.get('{0}/users/{1}/users/self/followed-by?access_token={1}'.format(self.url, self.access_token))
        return r.text

    def follows(self):
        r = requests.get('{0}/users/{1}/users/self/follows?access_token={1}'.format(self.url, self.access_token))
        return r.text

    def locations(self, location_id):
        r = requests.get('{0}/locations/{1}?access_token={2}'.format(self.url, location_id, self.access_token))
        return r.text

    def locations_media_recent(self, location_id):
        r = requests.get('{0}/locations/{1}/media/recent?access_token={2}'.format(self.url, location_id, self.access_token))
        return r.text

    def locations_search(self, lat, lng):
        r = requests.get('{0}/locations/search?lat={1}&lng={2}&access_token={3}'.format(self.url, lat, lng, self.access_token))
        return r.text
