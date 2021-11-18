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


class ArduinoTimezone(object):
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
        'name': 'str',
        'offset': 'int'
    }

    attribute_map = {
        'name': 'name',
        'offset': 'offset'
    }

    def __init__(self, name=None, offset=None, local_vars_configuration=None):  # noqa: E501
        """ArduinoTimezone - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._offset = None
        self.discriminator = None

        self.name = name
        self.offset = offset

    @property
    def name(self):
        """Gets the name of this ArduinoTimezone.  # noqa: E501

        Name of the time zone.  # noqa: E501

        :return: The name of this ArduinoTimezone.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ArduinoTimezone.

        Name of the time zone.  # noqa: E501

        :param name: The name of this ArduinoTimezone.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def offset(self):
        """Gets the offset of this ArduinoTimezone.  # noqa: E501

        Current UTC DST offset in seconds.  # noqa: E501

        :return: The offset of this ArduinoTimezone.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ArduinoTimezone.

        Current UTC DST offset in seconds.  # noqa: E501

        :param offset: The offset of this ArduinoTimezone.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and offset is None:  # noqa: E501
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501

        self._offset = offset

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
        if not isinstance(other, ArduinoTimezone):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ArduinoTimezone):
            return True

        return self.to_dict() != other.to_dict()
