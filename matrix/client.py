# -*- coding: utf-8 -*-
from .api import MatrixApi


class MatrixClient(object):
    """ The client API for Matrix. For the raw HTTP calls, see MatrixHttpApi.

    Usage (new user):
        client = MatrixClient("https://matrix.org")
        token = client.register_with_password(username="foobar", password="monkey")
        room = client.create_room("myroom")
        room.send_image(file_like_object)

    Usage (logged in):
        client = MatrixClient("https://matrix.org", token="foobar")
        rooms = client.get_rooms()  # NB: From initial sync
        client.add_listener(func)  # NB: event stream callback
        rooms[0].add_listener(func)  # NB: callbacks just for this room.
        room = client.join_room("#matrix:matrix.org")
        response = room.send_message("Hello!")
        response = room.kick("@bob:matrix.org")

    Incoming event callbacks (scopes):

        def user_callback(user, incoming_event):
            pass

        def room_callback(room, incoming_event):
            pass

        def global_callback(incoming_event):
            pass

    """

    def __init__(self, base_url, token=None):
        self.api = MatrixApi(base_url, token)
        self.rooms = {
            # room_id: Room
        }

    def register_with_password(self, username, password):
        response = self.api.register(
            "m.login.password", user=username, password=password
        )
        self.user_id = response.user_id
        self.token = response.access_token
        self.hs = response.home_server
        return self.token

    def create_room(self, alias=None, is_public=False, invitees=()):
        response = self.api.create_room(alias, is_public, invitees)
        return self._mkroom(response.room_id)

    def _mkroom(self, room_id):
        self.rooms[room_id] = Room(room_id)


class Room(object):

    def __init__(self, room_id):
        self.room_id = room_id


