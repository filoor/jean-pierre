#! /usr/bin/env python3
# coding: utf-8
"""
Jean-Pierre [Prototype]
A Raspberry Pi robot helping people to build groceries list.
Matteo Cargnelutti - github.com/matteocargnelutti

utils/cls.py - SQlite connector
"""
#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------
import os
import re
import sqlite3

#-----------------------------------------------------------------------------
# Database class
#-----------------------------------------------------------------------------
class Database:
    """
    This class handles :
    - Provides a link and a cursor to the database as class attributes
    Usage :
    - Database.on()
    - Database.CURSOR.execute(query, params)
    - ... etc
    - Database.off()
    Available class attributes :
    - LINK
    - CURSOR
    - FILE (path to the database file)
    """
    @classmethod
    def on(cls, alternate_file=''):
        """
        Connect to the database
        :param memory_mode: If True, creates a temporary database in memory
        :rtype: bool
        """
        # Path to the database
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path = path.replace('/utils', '')

        # Normal database
        if not alternate_file:
            cls.FILE = path + "/database.db"
        elif alternate_file == ':memory:':
            cls.FILE = ':memory:'
        else:
            alternate_file = alternate_file.replace('..', '')
            alternate_file = alternate_file.replace('/', '')
            cls.FILE = path + "/" + alternate_file

        # Connect
        cls.LINK = sqlite3.connect(cls.FILE)
        cls.LINK.row_factory = sqlite3.Row

        # Cursor
        cls.CURSOR = cls.LINK.cursor()

        return True

    @classmethod
    def off(cls):
        """
        Ends connection with the cls.
        :rtype: bool
        """
        cls.LINK.close()
        cls.LINK = None
        cls.CURSOR = None
        return True

    @classmethod
    def is_ready(cls):
        """
        Is the connection open ?
        :rtype: bool
        """
        return hasattr(cls, 'LINK')
