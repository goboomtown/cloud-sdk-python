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


class IssueStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        IssueStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'created': 'datetime',
            'type': 'str',
            'status': 'str',
            'resolution': 'str',
            'scheduled_time': 'str',
            'ticket_summary_text': 'str',
            'history_summary_text': 'str'
        }

        self.attribute_map = {
            'created': 'created',
            'type': 'type',
            'status': 'status',
            'resolution': 'resolution',
            'scheduled_time': 'scheduled_time',
            'ticket_summary_text': 'ticketSummaryText',
            'history_summary_text': 'historySummaryText'
        }

        self._created = None
        self._type = None
        self._status = None
        self._resolution = None
        self._scheduled_time = None
        self._ticket_summary_text = None
        self._history_summary_text = None

    @property
    def created(self):
        """
        Gets the created of this IssueStatus.
        Date created.

        :return: The created of this IssueStatus.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this IssueStatus.
        Date created.

        :param created: The created of this IssueStatus.
        :type: datetime
        """
        self._created = created

    @property
    def type(self):
        """
        Gets the type of this IssueStatus.
        The type of Issue this log is associated to.

        :return: The type of this IssueStatus.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this IssueStatus.
        The type of Issue this log is associated to.

        :param type: The type of this IssueStatus.
        :type: str
        """
        self._type = type

    @property
    def status(self):
        """
        Gets the status of this IssueStatus.
        The status of the issue.

        :return: The status of this IssueStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this IssueStatus.
        The status of the issue.

        :param status: The status of this IssueStatus.
        :type: str
        """
        self._status = status

    @property
    def resolution(self):
        """
        Gets the resolution of this IssueStatus.
        Resolution type.

        :return: The resolution of this IssueStatus.
        :rtype: str
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """
        Sets the resolution of this IssueStatus.
        Resolution type.

        :param resolution: The resolution of this IssueStatus.
        :type: str
        """
        self._resolution = resolution

    @property
    def scheduled_time(self):
        """
        Gets the scheduled_time of this IssueStatus.
        Scheduled date/time.

        :return: The scheduled_time of this IssueStatus.
        :rtype: str
        """
        return self._scheduled_time

    @scheduled_time.setter
    def scheduled_time(self, scheduled_time):
        """
        Sets the scheduled_time of this IssueStatus.
        Scheduled date/time.

        :param scheduled_time: The scheduled_time of this IssueStatus.
        :type: str
        """
        self._scheduled_time = scheduled_time

    @property
    def ticket_summary_text(self):
        """
        Gets the ticket_summary_text of this IssueStatus.
        Text describing the issue status/log event.

        :return: The ticket_summary_text of this IssueStatus.
        :rtype: str
        """
        return self._ticket_summary_text

    @ticket_summary_text.setter
    def ticket_summary_text(self, ticket_summary_text):
        """
        Sets the ticket_summary_text of this IssueStatus.
        Text describing the issue status/log event.

        :param ticket_summary_text: The ticket_summary_text of this IssueStatus.
        :type: str
        """
        self._ticket_summary_text = ticket_summary_text

    @property
    def history_summary_text(self):
        """
        Gets the history_summary_text of this IssueStatus.
        Text describing the issue status/log event.

        :return: The history_summary_text of this IssueStatus.
        :rtype: str
        """
        return self._history_summary_text

    @history_summary_text.setter
    def history_summary_text(self, history_summary_text):
        """
        Sets the history_summary_text of this IssueStatus.
        Text describing the issue status/log event.

        :param history_summary_text: The history_summary_text of this IssueStatus.
        :type: str
        """
        self._history_summary_text = history_summary_text

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
