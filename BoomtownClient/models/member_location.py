# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class MemberLocation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        MemberLocation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'members_id': 'str',
            'street_1': 'str',
            'street_2': 'str',
            'city': 'str',
            'state': 'str',
            'zipcode': 'str',
            'latitude': 'float',
            'longitude': 'float',
            'phone': 'str',
            'site_name': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'members_id': 'members_id',
            'street_1': 'street_1',
            'street_2': 'street_2',
            'city': 'city',
            'state': 'state',
            'zipcode': 'zipcode',
            'latitude': 'latitude',
            'longitude': 'longitude',
            'phone': 'phone',
            'site_name': 'site_name'
        }

        self._id = None
        self._members_id = None
        self._street_1 = None
        self._street_2 = None
        self._city = None
        self._state = None
        self._zipcode = None
        self._latitude = None
        self._longitude = None
        self._phone = None
        self._site_name = None

    @property
    def id(self):
        """
        Gets the id of this MemberLocation.
        Primary key.

        :return: The id of this MemberLocation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MemberLocation.
        Primary key.

        :param id: The id of this MemberLocation.
        :type: str
        """
        self._id = id

    @property
    def members_id(self):
        """
        Gets the members_id of this MemberLocation.
        The primary key of the related *Merchant*.

        :return: The members_id of this MemberLocation.
        :rtype: str
        """
        return self._members_id

    @members_id.setter
    def members_id(self, members_id):
        """
        Sets the members_id of this MemberLocation.
        The primary key of the related *Merchant*.

        :param members_id: The members_id of this MemberLocation.
        :type: str
        """
        self._members_id = members_id

    @property
    def street_1(self):
        """
        Gets the street_1 of this MemberLocation.
        Street address.

        :return: The street_1 of this MemberLocation.
        :rtype: str
        """
        return self._street_1

    @street_1.setter
    def street_1(self, street_1):
        """
        Sets the street_1 of this MemberLocation.
        Street address.

        :param street_1: The street_1 of this MemberLocation.
        :type: str
        """
        self._street_1 = street_1

    @property
    def street_2(self):
        """
        Gets the street_2 of this MemberLocation.
        Street address continued.

        :return: The street_2 of this MemberLocation.
        :rtype: str
        """
        return self._street_2

    @street_2.setter
    def street_2(self, street_2):
        """
        Sets the street_2 of this MemberLocation.
        Street address continued.

        :param street_2: The street_2 of this MemberLocation.
        :type: str
        """
        self._street_2 = street_2

    @property
    def city(self):
        """
        Gets the city of this MemberLocation.
        City.

        :return: The city of this MemberLocation.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this MemberLocation.
        City.

        :param city: The city of this MemberLocation.
        :type: str
        """
        self._city = city

    @property
    def state(self):
        """
        Gets the state of this MemberLocation.
        State Identifier (2 char code).

        :return: The state of this MemberLocation.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this MemberLocation.
        State Identifier (2 char code).

        :param state: The state of this MemberLocation.
        :type: str
        """
        self._state = state

    @property
    def zipcode(self):
        """
        Gets the zipcode of this MemberLocation.
        Postal Code.

        :return: The zipcode of this MemberLocation.
        :rtype: str
        """
        return self._zipcode

    @zipcode.setter
    def zipcode(self, zipcode):
        """
        Sets the zipcode of this MemberLocation.
        Postal Code.

        :param zipcode: The zipcode of this MemberLocation.
        :type: str
        """
        self._zipcode = zipcode

    @property
    def latitude(self):
        """
        Gets the latitude of this MemberLocation.
        Latitude.

        :return: The latitude of this MemberLocation.
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """
        Sets the latitude of this MemberLocation.
        Latitude.

        :param latitude: The latitude of this MemberLocation.
        :type: float
        """
        self._latitude = latitude

    @property
    def longitude(self):
        """
        Gets the longitude of this MemberLocation.
        Longitude.

        :return: The longitude of this MemberLocation.
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """
        Sets the longitude of this MemberLocation.
        Longitude.

        :param longitude: The longitude of this MemberLocation.
        :type: float
        """
        self._longitude = longitude

    @property
    def phone(self):
        """
        Gets the phone of this MemberLocation.
        Phone number.

        :return: The phone of this MemberLocation.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this MemberLocation.
        Phone number.

        :param phone: The phone of this MemberLocation.
        :type: str
        """
        self._phone = phone

    @property
    def site_name(self):
        """
        Gets the site_name of this MemberLocation.
        Informal reference, an alias.

        :return: The site_name of this MemberLocation.
        :rtype: str
        """
        return self._site_name

    @site_name.setter
    def site_name(self, site_name):
        """
        Sets the site_name of this MemberLocation.
        Informal reference, an alias.

        :param site_name: The site_name of this MemberLocation.
        :type: str
        """
        self._site_name = site_name

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

