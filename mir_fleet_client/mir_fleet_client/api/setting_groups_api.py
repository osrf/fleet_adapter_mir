"""
    2.13.5.3 FLEET REST API

    The REST API for the 2.13.5.3 interface of FLEET  # noqa: E501

    The version of the OpenAPI document: 2.13.5.3
    Contact: support@mir-robots.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from mir_fleet_client.api_client import ApiClient, Endpoint as _Endpoint
from mir_fleet_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from mir_fleet_client.model.error import Error
from mir_fleet_client.model.get_setting_group import GetSettingGroup
from mir_fleet_client.model.get_setting_group_advanced_settings import GetSettingGroupAdvancedSettings
from mir_fleet_client.model.get_setting_group_settings import GetSettingGroupSettings
from mir_fleet_client.model.get_setting_groups import GetSettingGroups


class SettingGroupsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.setting_groups_get_endpoint = _Endpoint(
            settings={
                'response_type': ([GetSettingGroups],),
                'auth': [
                    'Basic'
                ],
                'endpoint_path': '/setting_groups',
                'operation_id': 'setting_groups_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'accept_language',
                ],
                'required': [
                    'accept_language',
                ],
                'nullable': [
                ],
                'enum': [
                    'accept_language',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('accept_language',): {

                        "EN_US": "en_US",
                        "DE_DE": "de_DE",
                        "ES_ES": "es_ES",
                        "DA_DK": "da_DK",
                        "ZH_CN": "zh_CN"
                    },
                },
                'openapi_types': {
                    'accept_language':
                        (str,),
                },
                'attribute_map': {
                    'accept_language': 'Accept-Language',
                },
                'location_map': {
                    'accept_language': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.setting_groups_id_get_endpoint = _Endpoint(
            settings={
                'response_type': (GetSettingGroup,),
                'auth': [
                    'Basic'
                ],
                'endpoint_path': '/setting_groups/{id}',
                'operation_id': 'setting_groups_id_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'accept_language',
                    'id',
                ],
                'required': [
                    'accept_language',
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                    'accept_language',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('accept_language',): {

                        "EN_US": "en_US",
                        "DE_DE": "de_DE",
                        "ES_ES": "es_ES",
                        "DA_DK": "da_DK",
                        "ZH_CN": "zh_CN"
                    },
                },
                'openapi_types': {
                    'accept_language':
                        (str,),
                    'id':
                        (str,),
                },
                'attribute_map': {
                    'accept_language': 'Accept-Language',
                    'id': 'id',
                },
                'location_map': {
                    'accept_language': 'header',
                    'id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.setting_groups_settings_group_id_settings_advanced_get_endpoint = _Endpoint(
            settings={
                'response_type': ([GetSettingGroupAdvancedSettings],),
                'auth': [
                    'Basic'
                ],
                'endpoint_path': '/setting_groups/{settings_group_id}/settings/advanced',
                'operation_id': 'setting_groups_settings_group_id_settings_advanced_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'accept_language',
                    'settings_group_id',
                ],
                'required': [
                    'accept_language',
                    'settings_group_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'accept_language',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('accept_language',): {

                        "EN_US": "en_US",
                        "DE_DE": "de_DE",
                        "ES_ES": "es_ES",
                        "DA_DK": "da_DK",
                        "ZH_CN": "zh_CN"
                    },
                },
                'openapi_types': {
                    'accept_language':
                        (str,),
                    'settings_group_id':
                        (int,),
                },
                'attribute_map': {
                    'accept_language': 'Accept-Language',
                    'settings_group_id': 'settings_group_id',
                },
                'location_map': {
                    'accept_language': 'header',
                    'settings_group_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.setting_groups_settings_group_id_settings_get_endpoint = _Endpoint(
            settings={
                'response_type': ([GetSettingGroupSettings],),
                'auth': [
                    'Basic'
                ],
                'endpoint_path': '/setting_groups/{settings_group_id}/settings',
                'operation_id': 'setting_groups_settings_group_id_settings_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'accept_language',
                    'settings_group_id',
                ],
                'required': [
                    'accept_language',
                    'settings_group_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'accept_language',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('accept_language',): {

                        "EN_US": "en_US",
                        "DE_DE": "de_DE",
                        "ES_ES": "es_ES",
                        "DA_DK": "da_DK",
                        "ZH_CN": "zh_CN"
                    },
                },
                'openapi_types': {
                    'accept_language':
                        (str,),
                    'settings_group_id':
                        (int,),
                },
                'attribute_map': {
                    'accept_language': 'Accept-Language',
                    'settings_group_id': 'settings_group_id',
                },
                'location_map': {
                    'accept_language': 'header',
                    'settings_group_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def setting_groups_get(
        self,
        accept_language="en_US",
        **kwargs
    ):
        """GET /setting_groups  # noqa: E501

        Retrieve a list with the settings groups  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.setting_groups_get(accept_language="en_US", async_req=True)
        >>> result = thread.get()

        Args:
            accept_language (str): Language header. defaults to "en_US", must be one of ["en_US"]

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            [GetSettingGroups]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['accept_language'] = \
            accept_language
        return self.setting_groups_get_endpoint.call_with_http_info(**kwargs)

    def setting_groups_id_get(
        self,
        id,
        accept_language="en_US",
        **kwargs
    ):
        """GET /setting_groups/{id}  # noqa: E501

        Retrieve the details about the settings group with the specified ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.setting_groups_id_get(id, accept_language="en_US", async_req=True)
        >>> result = thread.get()

        Args:
            id (str): The id to search for
            accept_language (str): Language header. defaults to "en_US", must be one of ["en_US"]

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            GetSettingGroup
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['accept_language'] = \
            accept_language
        kwargs['id'] = \
            id
        return self.setting_groups_id_get_endpoint.call_with_http_info(**kwargs)

    def setting_groups_settings_group_id_settings_advanced_get(
        self,
        settings_group_id,
        accept_language="en_US",
        **kwargs
    ):
        """GET /setting_groups/{settings_group_id}/settings/advanced  # noqa: E501

        Retrieve the list of advanced settings from the settings group with the specified settings group ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.setting_groups_settings_group_id_settings_advanced_get(settings_group_id, accept_language="en_US", async_req=True)
        >>> result = thread.get()

        Args:
            settings_group_id (int): The settings_group_id to search for
            accept_language (str): Language header. defaults to "en_US", must be one of ["en_US"]

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            [GetSettingGroupAdvancedSettings]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['accept_language'] = \
            accept_language
        kwargs['settings_group_id'] = \
            settings_group_id
        return self.setting_groups_settings_group_id_settings_advanced_get_endpoint.call_with_http_info(**kwargs)

    def setting_groups_settings_group_id_settings_get(
        self,
        settings_group_id,
        accept_language="en_US",
        **kwargs
    ):
        """GET /setting_groups/{settings_group_id}/settings  # noqa: E501

        Retrieve the list of settings from the settings group with the specified settings group ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.setting_groups_settings_group_id_settings_get(settings_group_id, accept_language="en_US", async_req=True)
        >>> result = thread.get()

        Args:
            settings_group_id (int): The settings_group_id to search for
            accept_language (str): Language header. defaults to "en_US", must be one of ["en_US"]

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            [GetSettingGroupSettings]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['accept_language'] = \
            accept_language
        kwargs['settings_group_id'] = \
            settings_group_id
        return self.setting_groups_settings_group_id_settings_get_endpoint.call_with_http_info(**kwargs)
