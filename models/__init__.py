#!/usr/bin/python3
"""Package initializer"""
from models.engine.custom_file_storage import CustomFileStorage

storage_instance = CustomFileStorage()
storage_instance.reload_data()
