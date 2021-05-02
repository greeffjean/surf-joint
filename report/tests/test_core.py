from datetime import datetime
import sys

from django.test import TestCase
from django.urls import reverse

from report.models import Products, Locations, Members
from report.views import home, get_context

import pytest

from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_view(client):
    url = reverse('locations')
    response = client.get(url)

    assert response.status_code == 200


# async def test_context():
#     response = await self.async_client.get('')
#
#     self.assertIsNotNone(response.context['members'])
#     self.assertIsNotNone(response.context['products'])
#     self.assertIsNotNone(response.context['locations'])
#
#
# def test_view():
#     response = self.client.get('/add_product/')
#
#     assert response.status_code == 200
#
#
# def test_form_submisson():
#     data = {
#         'item': "item",
#         'category': 'category',
#         'price': 'R1',
#         'used': 'True',
#         'warranty': 'NA',
#         'images': '',
#         'date_posted': datetime.now()
#     }
#
#     response = self.client.post(
#         "/save_product/", data=data
#     )
#
#     assert response.status_code == 200
