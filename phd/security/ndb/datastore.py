# -*- coding: utf-8 -*-
"""
.. module:: flask_security_ndb
   :synopsis: Google App Engine NDB support for Flask-Security
The :mod:`<flask_security_ndb>` module adds support for the Google
App Engine datastore using NDB
"""
from flask_security import datastore


class NDBDatastore(datastore.Datastore):
    """Datastore adapter for NDB"""

    def __init__(self, *args, **kwargs):
        """No need to set self.db"""
        pass

    def put(self, model):
        """Saves a model to the datastore
        :param ndb.Model model: The model to save
        :return: The new entity
        :rtype: ndb.Model
        """
        model.put()
        return model

    def delete(self, model):
        """Deletes a model
        :param ndb.Model model: The ndb entity to delete
        """
        model.key.delete()


class NDBUserDatastore(NDBDatastore, datastore.UserDatastore):
    """An NDB datastore implementation for Flask-Security."""

    def __init__(self, user_model, role_model):
        """Initializes the User Datastore.
        :param ndb.Model user_model: A user model class definition
        :param ndb.Model role_model: A role model class definition
        """
        NDBDatastore.__init__(self)
        datastore.UserDatastore.__init__(self, user_model, role_model)

    def create_user(self, **kwargs):
        """App Engine override to set email as the :class:`ndb.Key`'s id"""
        kwargs["id"] = kwargs.get("email", None)
        return super(NDBUserDatastore, self).create_user(**kwargs)

    def create_role(self, **kwargs):
        """App Engine override to set name as the :class:`ndb.Key`'s id"""
        kwargs["id"] = kwargs.get("name", None)
        return super(NDBUserDatastore, self).create_role(**kwargs)

    def get_user(self, id_or_email):
        """Returns a user matching the specified ID or email address.
        :param str id_or_email: User's ID (email address)
        :rtype: User or None
        """
        return self.user_model.get_by_id(id_or_email)

    def find_user(self, **kwargs):
        """Returns a user matching the provided parameters.
        :rtype: User or None
        """
        if "id" in kwargs:
            return self.get_user(kwargs["id"])
        filters = [
            getattr(self.user_model, k) == v
            for k, v in kwargs.iteritems()
            if hasattr(self.user_model, k)
        ]
        return self.user_model.query(*filters).get()

    def find_role(self, role):
        """Returns a role matching the provided name.
        :param str role: Role name
        :rtype: Role or None
        """
        return self.role_model.get_by_id(role)
