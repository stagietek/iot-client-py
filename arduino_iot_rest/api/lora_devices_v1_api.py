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


class LoraDevicesV1Api(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def lora_devices_v1_create(self, create_lora_devices_v1_payload, **kwargs):  # noqa: E501
        """create lora_devices_v1  # noqa: E501

        Create a new lora device. Its info are saved on our database, and on the lora provider network. Creates a device_v2 automatically  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lora_devices_v1_create(create_lora_devices_v1_payload, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CreateLoraDevicesV1Payload create_lora_devices_v1_payload: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ArduinoLoradevicev1
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.lora_devices_v1_create_with_http_info(create_lora_devices_v1_payload, **kwargs)  # noqa: E501

    def lora_devices_v1_create_with_http_info(self, create_lora_devices_v1_payload, **kwargs):  # noqa: E501
        """create lora_devices_v1  # noqa: E501

        Create a new lora device. Its info are saved on our database, and on the lora provider network. Creates a device_v2 automatically  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lora_devices_v1_create_with_http_info(create_lora_devices_v1_payload, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CreateLoraDevicesV1Payload create_lora_devices_v1_payload: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ArduinoLoradevicev1, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'create_lora_devices_v1_payload'
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
                    " to method lora_devices_v1_create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'create_lora_devices_v1_payload' is set
        if self.api_client.client_side_validation and ('create_lora_devices_v1_payload' not in local_var_params or  # noqa: E501
                                                        local_var_params['create_lora_devices_v1_payload'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `create_lora_devices_v1_payload` when calling `lora_devices_v1_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_lora_devices_v1_payload' in local_var_params:
            body_params = local_var_params['create_lora_devices_v1_payload']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/lora-devices/', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ArduinoLoradevicev1',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
