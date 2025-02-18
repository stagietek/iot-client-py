# coding: utf-8

"""
    Arduino IoT Cloud API

     Provides a set of endpoints to manage Arduino IoT Cloud **Devices**, **Things**, **Properties** and **Timeseries**. This API can be called just with any HTTP Client, or using one of these clients:  * [Javascript NPM package](https://www.npmjs.com/package/@arduino/arduino-iot-client)  * [Python PYPI Package](https://pypi.org/project/arduino-iot-client/)  * [Golang Module](https://github.com/arduino/iot-client-go)  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from arduino_iot_rest.api_client import ApiClient
from arduino_iot_rest.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DevicesV2OtaApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def devices_v2_ota_send(self, id, devicev2_otabinaryurl, **kwargs):  # noqa: E501
        """send devices_v2_ota  # noqa: E501

        Send a binary url to a device  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.devices_v2_ota_send(id, devicev2_otabinaryurl, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: The id of the device (required)
        :param Devicev2Otabinaryurl devicev2_otabinaryurl: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.devices_v2_ota_send_with_http_info(id, devicev2_otabinaryurl, **kwargs)  # noqa: E501

    def devices_v2_ota_send_with_http_info(self, id, devicev2_otabinaryurl, **kwargs):  # noqa: E501
        """send devices_v2_ota  # noqa: E501

        Send a binary url to a device  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.devices_v2_ota_send_with_http_info(id, devicev2_otabinaryurl, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: The id of the device (required)
        :param Devicev2Otabinaryurl devicev2_otabinaryurl: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'id',
            'devicev2_otabinaryurl'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method devices_v2_ota_send" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `devices_v2_ota_send`")  # noqa: E501
        # verify the required parameter 'devicev2_otabinaryurl' is set
        if self.api_client.client_side_validation and ('devicev2_otabinaryurl' not in local_var_params or  # noqa: E501
                                                        local_var_params['devicev2_otabinaryurl'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `devicev2_otabinaryurl` when calling `devices_v2_ota_send`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'devicev2_otabinaryurl' in local_var_params:
            body_params = local_var_params['devicev2_otabinaryurl']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/v2/devices/{id}/ota', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def devices_v2_ota_upload(self, id, ota_file, **kwargs):  # noqa: E501
        """upload devices_v2_ota  # noqa: E501

        Upload a binary and send it to a device  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.devices_v2_ota_upload(id, ota_file, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: The id of the device (required)
        :param file ota_file: OTA file (required)
        :param bool _async: If false, wait for the full OTA process, until it gets a result from the device
        :param int expire_in_mins: Binary expire time in minutes, default 10 mins
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.devices_v2_ota_upload_with_http_info(id, ota_file, **kwargs)  # noqa: E501

    def devices_v2_ota_upload_with_http_info(self, id, ota_file, **kwargs):  # noqa: E501
        """upload devices_v2_ota  # noqa: E501

        Upload a binary and send it to a device  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.devices_v2_ota_upload_with_http_info(id, ota_file, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: The id of the device (required)
        :param file ota_file: OTA file (required)
        :param bool _async: If false, wait for the full OTA process, until it gets a result from the device
        :param int expire_in_mins: Binary expire time in minutes, default 10 mins
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'id',
            'ota_file',
            '_async',
            'expire_in_mins'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method devices_v2_ota_upload" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `devices_v2_ota_upload`")  # noqa: E501
        # verify the required parameter 'ota_file' is set
        if self.api_client.client_side_validation and ('ota_file' not in local_var_params or  # noqa: E501
                                                        local_var_params['ota_file'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `ota_file` when calling `devices_v2_ota_upload`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if '_async' in local_var_params:
            form_params.append(('async', local_var_params['_async']))  # noqa: E501
        if 'expire_in_mins' in local_var_params:
            form_params.append(('expire_in_mins', local_var_params['expire_in_mins']))  # noqa: E501
        if 'ota_file' in local_var_params:
            local_var_files['ota_file'] = local_var_params['ota_file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/v2/devices/{id}/ota', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
