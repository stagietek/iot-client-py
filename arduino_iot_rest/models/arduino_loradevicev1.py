# coding: utf-8

"""
    Arduino IoT Cloud API

     Provides a set of endpoints to manage Arduino IoT Cloud **Devices**, **Things**, **Properties** and **Timeseries**. This API can be called just with any HTTP Client, or using one of these clients:  * [Javascript NPM package](https://www.npmjs.com/package/@arduino/arduino-iot-client)  * [Python PYPI Package](https://pypi.org/project/arduino-iot-client/)  * [Golang Module](https://github.com/arduino/iot-client-go)  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from arduino_iot_rest.configuration import Configuration


class ArduinoLoradevicev1(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'app_eui': 'str',
        'app_key': 'str',
        'device_id': 'str',
        'eui': 'str'
    }

    attribute_map = {
        'app_eui': 'app_eui',
        'app_key': 'app_key',
        'device_id': 'device_id',
        'eui': 'eui'
    }

    def __init__(self, app_eui=None, app_key=None, device_id=None, eui=None, local_vars_configuration=None):  # noqa: E501
        """ArduinoLoradevicev1 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._app_eui = None
        self._app_key = None
        self._device_id = None
        self._eui = None
        self.discriminator = None

        self.app_eui = app_eui
        self.app_key = app_key
        self.device_id = device_id
        self.eui = eui

    @property
    def app_eui(self):
        """Gets the app_eui of this ArduinoLoradevicev1.  # noqa: E501

        The eui of the app  # noqa: E501

        :return: The app_eui of this ArduinoLoradevicev1.  # noqa: E501
        :rtype: str
        """
        return self._app_eui

    @app_eui.setter
    def app_eui(self, app_eui):
        """Sets the app_eui of this ArduinoLoradevicev1.

        The eui of the app  # noqa: E501

        :param app_eui: The app_eui of this ArduinoLoradevicev1.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and app_eui is None:  # noqa: E501
            raise ValueError("Invalid value for `app_eui`, must not be `None`")  # noqa: E501

        self._app_eui = app_eui

    @property
    def app_key(self):
        """Gets the app_key of this ArduinoLoradevicev1.  # noqa: E501

        The key of the device  # noqa: E501

        :return: The app_key of this ArduinoLoradevicev1.  # noqa: E501
        :rtype: str
        """
        return self._app_key

    @app_key.setter
    def app_key(self, app_key):
        """Sets the app_key of this ArduinoLoradevicev1.

        The key of the device  # noqa: E501

        :param app_key: The app_key of this ArduinoLoradevicev1.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and app_key is None:  # noqa: E501
            raise ValueError("Invalid value for `app_key`, must not be `None`")  # noqa: E501

        self._app_key = app_key

    @property
    def device_id(self):
        """Gets the device_id of this ArduinoLoradevicev1.  # noqa: E501

        The id of the device  # noqa: E501

        :return: The device_id of this ArduinoLoradevicev1.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this ArduinoLoradevicev1.

        The id of the device  # noqa: E501

        :param device_id: The device_id of this ArduinoLoradevicev1.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and device_id is None:  # noqa: E501
            raise ValueError("Invalid value for `device_id`, must not be `None`")  # noqa: E501

        self._device_id = device_id

    @property
    def eui(self):
        """Gets the eui of this ArduinoLoradevicev1.  # noqa: E501

        The eui of the lora device  # noqa: E501

        :return: The eui of this ArduinoLoradevicev1.  # noqa: E501
        :rtype: str
        """
        return self._eui

    @eui.setter
    def eui(self, eui):
        """Sets the eui of this ArduinoLoradevicev1.

        The eui of the lora device  # noqa: E501

        :param eui: The eui of this ArduinoLoradevicev1.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and eui is None:  # noqa: E501
            raise ValueError("Invalid value for `eui`, must not be `None`")  # noqa: E501

        self._eui = eui

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ArduinoLoradevicev1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ArduinoLoradevicev1):
            return True

        return self.to_dict() != other.to_dict()
