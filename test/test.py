# "contract test for trello board"
# import os
# import json
# import logging
# import atexit
# import unittest
# import pytest
# import requests
# from pact import Consumer, Provider, Format
# # Declaring logger
# log = logging.getLogger(__name__)
# logging.basicConfig(level=logging.INFO)
# print(Format().__dict__)
# # Setting up pact
# pact = Consumer('Consumer').has_pact_with(Provider('Provider'))
# pact.start_service()
# atexit.register(pact.stop_service)
# #setting up path for pact file
# CURR_FILE_PATH = os.path.dirname(os.path.abspath(__file__))
# PACT_DIR = os.path.join(CURR_FILE_PATH, '')
# PACT_FILE = os.path.join(PACT_DIR, 'pact.json')
# # Defining Class
# class GetBoard(unittest.TestCase):
# def test_get_board(self):
# """
# Defining test method
# """
# with open(os.path.join(PACT_DIR, PACT_FILE), 'rb') as pact_file:
# pact_file_json = json.load(pact_file)
# expected = pact_file_json
# (pact
# .given('Request to send message')
# .upon_receiving('a request for response for send message')
# .with_request('GET','/1/boards/1000')
# .will_respond_with(200, body=expected))
# with pact:
# result = requests.get(pact.uri + '/1/boards/1000')
# self.assertEqual(result.json(), expected)
# pact.verify()