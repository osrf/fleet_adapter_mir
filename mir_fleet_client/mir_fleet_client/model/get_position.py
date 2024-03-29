"""
    2.13.5.3 FLEET REST API

    The REST API for the 2.13.5.3 interface of FLEET  # noqa: E501

    The version of the OpenAPI document: 2.13.5.3
    Contact: support@mir-robots.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from mir_fleet_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from mir_fleet_client.exceptions import ApiAttributeError



class GetPosition(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'created_by': (str,),  # noqa: E501
            'created_by_id': (str,),  # noqa: E501
            'docking_offsets': (str,),  # noqa: E501
            'guid': (str,),  # noqa: E501
            'help_positions': (str,),  # noqa: E501
            'map': (str,),  # noqa: E501
            'map_id': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'orientation': (float,),  # noqa: E501
            'parent': (str, none_type,),  # noqa: E501
            'parent_id': (str, none_type,),  # noqa: E501
            'pos_x': (float,),  # noqa: E501
            'pos_y': (float,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'type_id': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'created_by': 'created_by',  # noqa: E501
        'created_by_id': 'created_by_id',  # noqa: E501
        'docking_offsets': 'docking_offsets',  # noqa: E501
        'guid': 'guid',  # noqa: E501
        'help_positions': 'help_positions',  # noqa: E501
        'map': 'map',  # noqa: E501
        'map_id': 'map_id',  # noqa: E501
        'name': 'name',  # noqa: E501
        'orientation': 'orientation',  # noqa: E501
        'parent': 'parent',  # noqa: E501
        'parent_id': 'parent_id',  # noqa: E501
        'pos_x': 'pos_x',  # noqa: E501
        'pos_y': 'pos_y',  # noqa: E501
        'type': 'type',  # noqa: E501
        'type_id': 'type_id',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """GetPosition - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            created_by (str): The url to the description of the type of this position. [optional]  # noqa: E501
            created_by_id (str): The global id of the user who created this entry. [optional]  # noqa: E501
            docking_offsets (str): The url to the possible docking offset. if the position does not have a docking offset then this field is empty. [optional]  # noqa: E501
            guid (str): The global id unique across robots that identifies this position. [optional]  # noqa: E501
            help_positions (str): . [optional]  # noqa: E501
            map (str): The url to the map this position belongs to. [optional]  # noqa: E501
            map_id (str): The global id of the map this positions belongs to. [optional]  # noqa: E501
            name (str): The name of the position. [optional]  # noqa: E501
            orientation (float): The orientation of the position in degrees relative to origo of the underlying map. [optional]  # noqa: E501
            parent (str, none_type): The url to the possible parent position. if the position does not have a parent position then this field is empty. [optional]  # noqa: E501
            parent_id (str, none_type): The global id of the possible parent position of the current position. a parent position is a position related to the current position, for instance the parent position of a trolley left entry position is the actual trolley position. if the position does not have a parent position then this field is empty. [optional]  # noqa: E501
            pos_x (float): The x-coordinate of the position relative to origo of the underlying map. [optional]  # noqa: E501
            pos_y (float): The y-coordinate of the position relative to origo of the underlying map. [optional]  # noqa: E501
            type (str): The url to the description of the type of this position. [optional]  # noqa: E501
            type_id (int): The type of position. see the general description above. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """GetPosition - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            created_by (str): The url to the description of the type of this position. [optional]  # noqa: E501
            created_by_id (str): The global id of the user who created this entry. [optional]  # noqa: E501
            docking_offsets (str): The url to the possible docking offset. if the position does not have a docking offset then this field is empty. [optional]  # noqa: E501
            guid (str): The global id unique across robots that identifies this position. [optional]  # noqa: E501
            help_positions (str): . [optional]  # noqa: E501
            map (str): The url to the map this position belongs to. [optional]  # noqa: E501
            map_id (str): The global id of the map this positions belongs to. [optional]  # noqa: E501
            name (str): The name of the position. [optional]  # noqa: E501
            orientation (float): The orientation of the position in degrees relative to origo of the underlying map. [optional]  # noqa: E501
            parent (str, none_type): The url to the possible parent position. if the position does not have a parent position then this field is empty. [optional]  # noqa: E501
            parent_id (str, none_type): The global id of the possible parent position of the current position. a parent position is a position related to the current position, for instance the parent position of a trolley left entry position is the actual trolley position. if the position does not have a parent position then this field is empty. [optional]  # noqa: E501
            pos_x (float): The x-coordinate of the position relative to origo of the underlying map. [optional]  # noqa: E501
            pos_y (float): The y-coordinate of the position relative to origo of the underlying map. [optional]  # noqa: E501
            type (str): The url to the description of the type of this position. [optional]  # noqa: E501
            type_id (int): The type of position. see the general description above. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
