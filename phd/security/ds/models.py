# -*- coding: utf-8 -*-
"""
.. module:: flask_security_ndb
   :synopsis: Google App Engine DS support for Flask-Security
The :mod:`<flask_security_ndb>` module adds support for the Google
App Engine datastore using GCP datastore
"""
from flask_security import UserMixin, RoleMixin

from google.cloud import datastore


class DSBase:
    def __init__(self, client, *args, **kwargs):
        self.client = client

    @property
    def id(self):
        """Override for getting the ID.
        :rtype: int
        """
        return self.id

    @classmethod
    def get_by_id(cls, client, base_id):
        key = client.key(cls.__name__, base_id)
        return client.get(key)


class Role(DSBase, RoleMixin):
    pass


class User(DSBase, UserMixin):
    def __init__(self, email, password, *args, **kwargs):
        self.email = email
        self.password = password
        for key, value in kwargs:
            setattr(self, key, value)
        self._roles_cache = []
        roles = [r.key for r in kwargs.pop("roles", [])]
        super().__init__(*args, **kwargs)
        self.roles_ = roles

    @property
    def roles(self):
        if len(self._roles_cache) != len(self.roles_):
            self._roles_cache = datastore.Client().get_multi(self.roles_)
        return self._roles_cache

    @roles.setter
    def roles(self, role):
        self._roles_cache.append(role)
        self.roles_.append(role.key)
