# -*- coding: utf-8 -*-
"""
.. module:: flask_security_ndb
   :synopsis: Google App Engine NDB support for Flask-Security
The :mod:`<flask_security_ndb>` module adds support for the Google
App Engine datastore using NDB
"""
from flask_security import UserMixin, RoleMixin
from google.appengine.ext import ndb


class NDBBase(ndb.Model):
    @property
    def id(self):
        """Override for getting the ID.
        Resolves NotImplementedError: No `id` attribute - override `get_id`
        :rtype: str
        """
        return self.key.id()


class Role(NDBBase, RoleMixin):
    name = ndb.StringProperty()
    description = ndb.StringProperty()


class User(NDBBase, UserMixin):
    email = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    active = ndb.BooleanProperty(default=True)
    confirmed_at = ndb.DateTimeProperty()
    last_login_at = ndb.DateTimeProperty()
    current_login_at = ndb.DateTimeProperty()
    last_login_ip = ndb.TextProperty()
    current_login_ip = ndb.TextProperty()
    login_count = ndb.IntegerProperty(indexed=False, default=0)
    roles_ = ndb.KeyProperty(Role, repeated=True)

    def __init__(self, *args, **kwargs):
        self._roles_cache = []
        roles = [r.key for r in kwargs.pop("roles", [])]
        super(User, self).__init__(*args, **kwargs)
        self.roles_ = roles

    @property
    def roles(self):
        if len(self._roles_cache) != len(self.roles_):
            self._roles_cache = ndb.get_multi(self.roles_)
        return self._roles_cache

    @roles.setter
    def roles(self, role):
        self._roles_cache.append(role)
        self.roles_.append(role.key)
