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


class ProviderTeamResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ProviderTeamResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'pages': 'int',
            'success': 'bool',
            'current_server_time': 'datetime',
            'total_count': 'int',
            'returned': 'int',
            'message': 'str',
            'results': 'list[ProviderTeam]'
        }

        self.attribute_map = {
            'pages': 'pages',
            'success': 'success',
            'current_server_time': 'current_server_time',
            'total_count': 'totalCount',
            'returned': 'returned',
            'message': 'message',
            'results': 'results'
        }

        self._pages = None
        self._success = None
        self._current_server_time = None
        self._total_count = None
        self._returned = None
        self._message = None
        self._results = None

    @property
    def pages(self):
        """
        Gets the pages of this ProviderTeamResponse.
        Total pages available.

        :return: The pages of this ProviderTeamResponse.
        :rtype: int
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """
        Sets the pages of this ProviderTeamResponse.
        Total pages available.

        :param pages: The pages of this ProviderTeamResponse.
        :type: int
        """
        self._pages = pages

    @property
    def success(self):
        """
        Gets the success of this ProviderTeamResponse.
        Indicates success of the operation.

        :return: The success of this ProviderTeamResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this ProviderTeamResponse.
        Indicates success of the operation.

        :param success: The success of this ProviderTeamResponse.
        :type: bool
        """
        self._success = success

    @property
    def current_server_time(self):
        """
        Gets the current_server_time of this ProviderTeamResponse.


        :return: The current_server_time of this ProviderTeamResponse.
        :rtype: datetime
        """
        return self._current_server_time

    @current_server_time.setter
    def current_server_time(self, current_server_time):
        """
        Sets the current_server_time of this ProviderTeamResponse.


        :param current_server_time: The current_server_time of this ProviderTeamResponse.
        :type: datetime
        """
        self._current_server_time = current_server_time

    @property
    def total_count(self):
        """
        Gets the total_count of this ProviderTeamResponse.
        Total records available.

        :return: The total_count of this ProviderTeamResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this ProviderTeamResponse.
        Total records available.

        :param total_count: The total_count of this ProviderTeamResponse.
        :type: int
        """
        self._total_count = total_count

    @property
    def returned(self):
        """
        Gets the returned of this ProviderTeamResponse.
        Total records retrieved.

        :return: The returned of this ProviderTeamResponse.
        :rtype: int
        """
        return self._returned

    @returned.setter
    def returned(self, returned):
        """
        Sets the returned of this ProviderTeamResponse.
        Total records retrieved.

        :param returned: The returned of this ProviderTeamResponse.
        :type: int
        """
        self._returned = returned

    @property
    def message(self):
        """
        Gets the message of this ProviderTeamResponse.


        :return: The message of this ProviderTeamResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ProviderTeamResponse.


        :param message: The message of this ProviderTeamResponse.
        :type: str
        """
        self._message = message

    @property
    def results(self):
        """
        Gets the results of this ProviderTeamResponse.


        :return: The results of this ProviderTeamResponse.
        :rtype: list[ProviderTeam]
        """
        return self._results

    @results.setter
    def results(self, results):
        """
        Sets the results of this ProviderTeamResponse.


        :param results: The results of this ProviderTeamResponse.
        :type: list[ProviderTeam]
        """
        self._results = results

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

