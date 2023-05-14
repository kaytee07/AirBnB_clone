#!/usr/bin/python3
"""
this is to create a unique file storage instance
"""

from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
