# coding: utf-8

"""
MerchantsApi.py
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
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class MerchantsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_member(self, body, **kwargs):
        """
        Creates a new Merchant
        Creates a *Merchant* and optionally *MerchantLocation* and *MerchantUser*

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_member(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param MemberCreateRequest body: The *Merchant* to create (required)
        :return: MemberCreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_member" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_member`")

        resource_path = '/members/create'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['X-Boomtown-Date', 'X-Boomtown-Signature', 'X-Boomtown-Token']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='MemberCreateResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_member(self, member_id, **kwargs):
        """
        Returns a Merchant
        Returns a *Merchant*

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_member(member_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str member_id: The primary key of the *Merchant* (required)
        :return: MemberResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['member_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_member" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'member_id' is set
        if ('member_id' not in params) or (params['member_id'] is None):
            raise ValueError("Missing the required parameter `member_id` when calling `get_member`")

        resource_path = '/members/get/{member_id}'.replace('{format}', 'json')
        path_params = {}
        if 'member_id' in params:
            path_params['member_id'] = params['member_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['X-Boomtown-Date', 'X-Boomtown-Signature', 'X-Boomtown-Token']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='MemberResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_member_location_users(self, member_id, **kwargs):
        """
        Returns a collection of MerchantUsers
        Returns a collection of *MerchantUsers* belonging to a *MerchantLocation*

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_member_location_users(member_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str member_id: The primary key of the *Merchant* (required)
        :return: MemberUserResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['member_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_member_location_users" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'member_id' is set
        if ('member_id' not in params) or (params['member_id'] is None):
            raise ValueError("Missing the required parameter `member_id` when calling `get_member_location_users`")

        resource_path = '/members/location/users/{member_id}'.replace('{format}', 'json')
        path_params = {}
        if 'member_id' in params:
            path_params['member_id'] = params['member_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['X-Boomtown-Date', 'X-Boomtown-Signature', 'X-Boomtown-Token']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='MemberUserResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_member_locations(self, member_id, **kwargs):
        """
        Returns a collection of MerchantLocations
        Returns a collection of *MerchantLocation* records belonging to a *Merchant*

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_member_locations(member_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str member_id: The primary key of the *Merchant* (required)
        :param str members_locations_id: An optional members_locations_id to filter the results with
        :return: MemberLocationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['member_id', 'members_locations_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_member_locations" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'member_id' is set
        if ('member_id' not in params) or (params['member_id'] is None):
            raise ValueError("Missing the required parameter `member_id` when calling `get_member_locations`")

        resource_path = '/members/location/get/{member_id}'.replace('{format}', 'json')
        path_params = {}
        if 'member_id' in params:
            path_params['member_id'] = params['member_id']

        query_params = {}
        if 'members_locations_id' in params:
            query_params['members_locations_id'] = params['members_locations_id']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['X-Boomtown-Date', 'X-Boomtown-Signature', 'X-Boomtown-Token']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='MemberLocationResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_member_meta_industries(self, **kwargs):
        """
        Returns collection of industries
        Returns the industries available for a *Merchant*

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_member_meta_industries(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: EnumerationItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_member_meta_industries" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/members/meta/industries'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['X-Boomtown-Date', 'X-Boomtown-Signature', 'X-Boomtown-Token']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='EnumerationItemResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_member_meta_statuses(self, **kwargs):
        """
        Returns collection of statuses
        Returns the statuses available for a *Merchant* or *MerchantUsers*

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_member_meta_statuses(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: EnumerationItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_member_meta_statuses" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/members/meta/statuses'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['X-Boomtown-Date', 'X-Boomtown-Signature', 'X-Boomtown-Token']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='EnumerationItemResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_member_users(self, member_id, **kwargs):
        """
        Returnsa a collection of MerchantUsers
        Returns a collection of *MerchantUser* records belonging to a *Merchant*

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_member_users(member_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str member_id: The id of the *Merchant* (required)
        :param str user_id: Optional user_id to filter the results with
        :return: MemberUserResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['member_id', 'user_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_member_users" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'member_id' is set
        if ('member_id' not in params) or (params['member_id'] is None):
            raise ValueError("Missing the required parameter `member_id` when calling `get_member_users`")

        resource_path = '/members/user/get/{member_id}'.replace('{format}', 'json')
        path_params = {}
        if 'member_id' in params:
            path_params['member_id'] = params['member_id']

        query_params = {}
        if 'user_id' in params:
            query_params['user_id'] = params['user_id']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['X-Boomtown-Date', 'X-Boomtown-Signature', 'X-Boomtown-Token']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='MemberUserResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
