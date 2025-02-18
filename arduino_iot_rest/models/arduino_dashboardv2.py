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


class ArduinoDashboardv2(object):
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
        'id': 'str',
        'name': 'str',
        'shared_by': 'ArduinoDashboardshare',
        'shared_with': 'list[ArduinoDashboardshare]',
        'updated_at': 'datetime',
        'widgets': 'list[ArduinoWidgetv2]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'shared_by': 'shared_by',
        'shared_with': 'shared_with',
        'updated_at': 'updated_at',
        'widgets': 'widgets'
    }

    def __init__(self, id=None, name=None, shared_by=None, shared_with=None, updated_at=None, widgets=None, local_vars_configuration=None):  # noqa: E501
        """ArduinoDashboardv2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._shared_by = None
        self._shared_with = None
        self._updated_at = None
        self._widgets = None
        self.discriminator = None

        self.id = id
        self.name = name
        if shared_by is not None:
            self.shared_by = shared_by
        if shared_with is not None:
            self.shared_with = shared_with
        self.updated_at = updated_at
        if widgets is not None:
            self.widgets = widgets

    @property
    def id(self):
        """Gets the id of this ArduinoDashboardv2.  # noqa: E501

        The friendly name of the dashboard  # noqa: E501

        :return: The id of this ArduinoDashboardv2.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ArduinoDashboardv2.

        The friendly name of the dashboard  # noqa: E501

        :param id: The id of this ArduinoDashboardv2.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this ArduinoDashboardv2.  # noqa: E501

        The friendly name of the dashboard  # noqa: E501

        :return: The name of this ArduinoDashboardv2.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ArduinoDashboardv2.

        The friendly name of the dashboard  # noqa: E501

        :param name: The name of this ArduinoDashboardv2.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def shared_by(self):
        """Gets the shared_by of this ArduinoDashboardv2.  # noqa: E501


        :return: The shared_by of this ArduinoDashboardv2.  # noqa: E501
        :rtype: ArduinoDashboardshare
        """
        return self._shared_by

    @shared_by.setter
    def shared_by(self, shared_by):
        """Sets the shared_by of this ArduinoDashboardv2.


        :param shared_by: The shared_by of this ArduinoDashboardv2.  # noqa: E501
        :type: ArduinoDashboardshare
        """

        self._shared_by = shared_by

    @property
    def shared_with(self):
        """Gets the shared_with of this ArduinoDashboardv2.  # noqa: E501

        ArduinoDashboardshareCollection is the media type for an array of ArduinoDashboardshare (default view)  # noqa: E501

        :return: The shared_with of this ArduinoDashboardv2.  # noqa: E501
        :rtype: list[ArduinoDashboardshare]
        """
        return self._shared_with

    @shared_with.setter
    def shared_with(self, shared_with):
        """Sets the shared_with of this ArduinoDashboardv2.

        ArduinoDashboardshareCollection is the media type for an array of ArduinoDashboardshare (default view)  # noqa: E501

        :param shared_with: The shared_with of this ArduinoDashboardv2.  # noqa: E501
        :type: list[ArduinoDashboardshare]
        """

        self._shared_with = shared_with

    @property
    def updated_at(self):
        """Gets the updated_at of this ArduinoDashboardv2.  # noqa: E501

        Last update date  # noqa: E501

        :return: The updated_at of this ArduinoDashboardv2.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ArduinoDashboardv2.

        Last update date  # noqa: E501

        :param updated_at: The updated_at of this ArduinoDashboardv2.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def widgets(self):
        """Gets the widgets of this ArduinoDashboardv2.  # noqa: E501

        ArduinoWidgetv2Collection is the media type for an array of ArduinoWidgetv2 (default view)  # noqa: E501

        :return: The widgets of this ArduinoDashboardv2.  # noqa: E501
        :rtype: list[ArduinoWidgetv2]
        """
        return self._widgets

    @widgets.setter
    def widgets(self, widgets):
        """Sets the widgets of this ArduinoDashboardv2.

        ArduinoWidgetv2Collection is the media type for an array of ArduinoWidgetv2 (default view)  # noqa: E501

        :param widgets: The widgets of this ArduinoDashboardv2.  # noqa: E501
        :type: list[ArduinoWidgetv2]
        """

        self._widgets = widgets

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
        if not isinstance(other, ArduinoDashboardv2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ArduinoDashboardv2):
            return True

        return self.to_dict() != other.to_dict()
