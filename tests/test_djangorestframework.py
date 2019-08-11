# -*- coding: utf-8 -*-
from rest_framework import APIClient, APIRequestFactory


def test_api_client(api_client):
    assert isinstance(api_client, APIClient)


def test_api_rf(api_rf):
    assert isinstance(api_rf, APIRequestFactory)
