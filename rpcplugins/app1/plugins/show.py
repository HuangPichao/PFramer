#!/usr/bin/python
# -*- coding: utf-8 -*-
from util.qbasemodel import ModelMetaclass

name = "show"

class Show(object):

    __metaclass__ = ModelMetaclass

    Fields = (
        ('model', str, "123"),
        ('brand', str, "456"),
        ('year', int),
        ('inStock', bool),
        ('d', dict, {'a': 1111})
    )

obj = Show()
