# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._config_servers_operations import (
    build_get_request,
    build_update_patch_request,
    build_update_put_request,
    build_validate_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ConfigServersOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.appplatform.v2023_07_01_preview.aio.AppPlatformManagementClient`'s
        :attr:`config_servers` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")
        self._api_version = input_args.pop(0) if input_args else kwargs.pop("api_version")

    @distributed_trace_async
    async def get(self, resource_group_name: str, service_name: str, **kwargs: Any) -> _models.ConfigServerResource:
        """Get the config server and its properties.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param service_name: The name of the Service resource. Required.
        :type service_name: str
        :return: ConfigServerResource or the result of cls(response)
        :rtype: ~azure.mgmt.appplatform.v2023_07_01_preview.models.ConfigServerResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2023-07-01-preview")
        )
        cls: ClsType[_models.ConfigServerResource] = kwargs.pop("cls", None)

        _request = build_get_request(
            resource_group_name=resource_group_name,
            service_name=service_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ConfigServerResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    async def _update_put_initial(
        self,
        resource_group_name: str,
        service_name: str,
        config_server_resource: Union[_models.ConfigServerResource, IO[bytes]],
        **kwargs: Any
    ) -> _models.ConfigServerResource:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2023-07-01-preview")
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ConfigServerResource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(config_server_resource, (IOBase, bytes)):
            _content = config_server_resource
        else:
            _json = self._serialize.body(config_server_resource, "ConfigServerResource")

        _request = build_update_put_request(
            resource_group_name=resource_group_name,
            service_name=service_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("ConfigServerResource", pipeline_response)

        if response.status_code == 202:
            deserialized = self._deserialize("ConfigServerResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def begin_update_put(
        self,
        resource_group_name: str,
        service_name: str,
        config_server_resource: _models.ConfigServerResource,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.ConfigServerResource]:
        """Update the config server.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param service_name: The name of the Service resource. Required.
        :type service_name: str
        :param config_server_resource: Parameters for the update operation. Required.
        :type config_server_resource:
         ~azure.mgmt.appplatform.v2023_07_01_preview.models.ConfigServerResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either ConfigServerResource or the result
         of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.appplatform.v2023_07_01_preview.models.ConfigServerResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_update_put(
        self,
        resource_group_name: str,
        service_name: str,
        config_server_resource: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.ConfigServerResource]:
        """Update the config server.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param service_name: The name of the Service resource. Required.
        :type service_name: str
        :param config_server_resource: Parameters for the update operation. Required.
        :type config_server_resource: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either ConfigServerResource or the result
         of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.appplatform.v2023_07_01_preview.models.ConfigServerResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_update_put(
        self,
        resource_group_name: str,
        service_name: str,
        config_server_resource: Union[_models.ConfigServerResource, IO[bytes]],
        **kwargs: Any
    ) -> AsyncLROPoller[_models.ConfigServerResource]:
        """Update the config server.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param service_name: The name of the Service resource. Required.
        :type service_name: str
        :param config_server_resource: Parameters for the update operation. Is either a
         ConfigServerResource type or a IO[bytes] type. Required.
        :type config_server_resource:
         ~azure.mgmt.appplatform.v2023_07_01_preview.models.ConfigServerResource or IO[bytes]
        :return: An instance of AsyncLROPoller that returns either ConfigServerResource or the result
         of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.appplatform.v2023_07_01_preview.models.ConfigServerResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2023-07-01-preview")
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ConfigServerResource] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._update_put_initial(
                resource_group_name=resource_group_name,
                service_name=service_name,
                config_server_resource=config_server_resource,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("ConfigServerResource", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        if polling is True:
            polling_method: AsyncPollingMethod = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[_models.ConfigServerResource].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[_models.ConfigServerResource](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    async def _update_patch_initial(
        self,
        resource_group_name: str,
        service_name: str,
        config_server_resource: Union[_models.ConfigServerResource, IO[bytes]],
        **kwargs: Any
    ) -> _models.ConfigServerResource:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2023-07-01-preview")
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ConfigServerResource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(config_server_resource, (IOBase, bytes)):
            _content = config_server_resource
        else:
            _json = self._serialize.body(config_server_resource, "ConfigServerResource")

        _request = build_update_patch_request(
            resource_group_name=resource_group_name,
            service_name=service_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("ConfigServerResource", pipeline_response)

        if response.status_code == 202:
            deserialized = self._deserialize("ConfigServerResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def begin_update_patch(
        self,
        resource_group_name: str,
        service_name: str,
        config_server_resource: _models.ConfigServerResource,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.ConfigServerResource]:
        """Update the config server.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param service_name: The name of the Service resource. Required.
        :type service_name: str
        :param config_server_resource: Parameters for the update operation. Required.
        :type config_server_resource:
         ~azure.mgmt.appplatform.v2023_07_01_preview.models.ConfigServerResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either ConfigServerResource or the result
         of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.appplatform.v2023_07_01_preview.models.ConfigServerResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_update_patch(
        self,
        resource_group_name: str,
        service_name: str,
        config_server_resource: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.ConfigServerResource]:
        """Update the config server.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param service_name: The name of the Service resource. Required.
        :type service_name: str
        :param config_server_resource: Parameters for the update operation. Required.
        :type config_server_resource: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either ConfigServerResource or the result
         of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.appplatform.v2023_07_01_preview.models.ConfigServerResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_update_patch(
        self,
        resource_group_name: str,
        service_name: str,
        config_server_resource: Union[_models.ConfigServerResource, IO[bytes]],
        **kwargs: Any
    ) -> AsyncLROPoller[_models.ConfigServerResource]:
        """Update the config server.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param service_name: The name of the Service resource. Required.
        :type service_name: str
        :param config_server_resource: Parameters for the update operation. Is either a
         ConfigServerResource type or a IO[bytes] type. Required.
        :type config_server_resource:
         ~azure.mgmt.appplatform.v2023_07_01_preview.models.ConfigServerResource or IO[bytes]
        :return: An instance of AsyncLROPoller that returns either ConfigServerResource or the result
         of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.appplatform.v2023_07_01_preview.models.ConfigServerResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2023-07-01-preview")
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ConfigServerResource] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._update_patch_initial(
                resource_group_name=resource_group_name,
                service_name=service_name,
                config_server_resource=config_server_resource,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("ConfigServerResource", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        if polling is True:
            polling_method: AsyncPollingMethod = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[_models.ConfigServerResource].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[_models.ConfigServerResource](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    async def _validate_initial(
        self,
        resource_group_name: str,
        service_name: str,
        config_server_settings: Union[_models.ConfigServerSettings, IO[bytes]],
        **kwargs: Any
    ) -> _models.ConfigServerSettingsValidateResult:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2023-07-01-preview")
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ConfigServerSettingsValidateResult] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(config_server_settings, (IOBase, bytes)):
            _content = config_server_settings
        else:
            _json = self._serialize.body(config_server_settings, "ConfigServerSettings")

        _request = build_validate_request(
            resource_group_name=resource_group_name,
            service_name=service_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("ConfigServerSettingsValidateResult", pipeline_response)

        if response.status_code == 202:
            deserialized = self._deserialize("ConfigServerSettingsValidateResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def begin_validate(
        self,
        resource_group_name: str,
        service_name: str,
        config_server_settings: _models.ConfigServerSettings,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.ConfigServerSettingsValidateResult]:
        """Check if the config server settings are valid.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param service_name: The name of the Service resource. Required.
        :type service_name: str
        :param config_server_settings: Config server settings to be validated. Required.
        :type config_server_settings:
         ~azure.mgmt.appplatform.v2023_07_01_preview.models.ConfigServerSettings
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either ConfigServerSettingsValidateResult
         or the result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.appplatform.v2023_07_01_preview.models.ConfigServerSettingsValidateResult]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_validate(
        self,
        resource_group_name: str,
        service_name: str,
        config_server_settings: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.ConfigServerSettingsValidateResult]:
        """Check if the config server settings are valid.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param service_name: The name of the Service resource. Required.
        :type service_name: str
        :param config_server_settings: Config server settings to be validated. Required.
        :type config_server_settings: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either ConfigServerSettingsValidateResult
         or the result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.appplatform.v2023_07_01_preview.models.ConfigServerSettingsValidateResult]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_validate(
        self,
        resource_group_name: str,
        service_name: str,
        config_server_settings: Union[_models.ConfigServerSettings, IO[bytes]],
        **kwargs: Any
    ) -> AsyncLROPoller[_models.ConfigServerSettingsValidateResult]:
        """Check if the config server settings are valid.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param service_name: The name of the Service resource. Required.
        :type service_name: str
        :param config_server_settings: Config server settings to be validated. Is either a
         ConfigServerSettings type or a IO[bytes] type. Required.
        :type config_server_settings:
         ~azure.mgmt.appplatform.v2023_07_01_preview.models.ConfigServerSettings or IO[bytes]
        :return: An instance of AsyncLROPoller that returns either ConfigServerSettingsValidateResult
         or the result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.appplatform.v2023_07_01_preview.models.ConfigServerSettingsValidateResult]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2023-07-01-preview")
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ConfigServerSettingsValidateResult] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._validate_initial(
                resource_group_name=resource_group_name,
                service_name=service_name,
                config_server_settings=config_server_settings,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("ConfigServerSettingsValidateResult", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod, AsyncARMPolling(lro_delay, lro_options={"final-state-via": "location"}, **kwargs)
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[_models.ConfigServerSettingsValidateResult].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[_models.ConfigServerSettingsValidateResult](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )
