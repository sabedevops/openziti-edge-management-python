# openziti_edge_management.TerminatorApi

All URIs are relative to *https://demo.ziti.dev/edge/management/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_terminator**](TerminatorApi.md#create_terminator) | **POST** /terminators | Create a terminator resource
[**delete_terminator**](TerminatorApi.md#delete_terminator) | **DELETE** /terminators/{id} | Delete a terminator
[**detail_terminator**](TerminatorApi.md#detail_terminator) | **GET** /terminators/{id} | Retrieves a single terminator
[**list_terminators**](TerminatorApi.md#list_terminators) | **GET** /terminators | List terminators
[**patch_terminator**](TerminatorApi.md#patch_terminator) | **PATCH** /terminators/{id} | Update the supplied fields on a terminator
[**update_terminator**](TerminatorApi.md#update_terminator) | **PUT** /terminators/{id} | Update all fields on a terminator


# **create_terminator**
> CreateEnvelope create_terminator(terminator)

Create a terminator resource

Create a terminator resource. Requires admin access.

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import terminator_api
from openziti_edge_management.model.create_envelope import CreateEnvelope
from openziti_edge_management.model.terminator_create import TerminatorCreate
from openziti_edge_management.model.api_error_envelope import ApiErrorEnvelope
from pprint import pprint
# Defining the host is optional and defaults to https://demo.ziti.dev/edge/management/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_management.Configuration(
    host = "https://demo.ziti.dev/edge/management/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ztSession
configuration.api_key['ztSession'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = terminator_api.TerminatorApi(api_client)
    terminator = TerminatorCreate(
        address="address_example",
        binding="binding_example",
        cost=TerminatorCost(0),
        identity="identity_example",
        identity_secret='YQ==',
        precedence=TerminatorPrecedence("default"),
        router="router_example",
        service="service_example",
        tags=Tags(None),
    ) # TerminatorCreate | A terminator to create

    # example passing only required values which don't have defaults set
    try:
        # Create a terminator resource
        api_response = api_instance.create_terminator(terminator)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling TerminatorApi->create_terminator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terminator** | [**TerminatorCreate**](TerminatorCreate.md)| A terminator to create |

### Return type

[**CreateEnvelope**](CreateEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The create request was successful and the resource has been added at the following location |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_terminator**
> Empty delete_terminator(id)

Delete a terminator

Delete a terminator by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import terminator_api
from openziti_edge_management.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_management.model.empty import Empty
from pprint import pprint
# Defining the host is optional and defaults to https://demo.ziti.dev/edge/management/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_management.Configuration(
    host = "https://demo.ziti.dev/edge/management/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ztSession
configuration.api_key['ztSession'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = terminator_api.TerminatorApi(api_client)
    id = "id_example" # str | The id of the requested resource

    # example passing only required values which don't have defaults set
    try:
        # Delete a terminator
        api_response = api_instance.delete_terminator(id)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling TerminatorApi->delete_terminator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |

### Return type

[**Empty**](Empty.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The delete request was successful and the resource has been removed |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**409** | The resource requested to be removed/altered cannot be as it is referenced by another object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detail_terminator**
> DetailTerminatorEnvelope detail_terminator(id)

Retrieves a single terminator

Retrieves a single terminator by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import terminator_api
from openziti_edge_management.model.detail_terminator_envelope import DetailTerminatorEnvelope
from openziti_edge_management.model.api_error_envelope import ApiErrorEnvelope
from pprint import pprint
# Defining the host is optional and defaults to https://demo.ziti.dev/edge/management/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_management.Configuration(
    host = "https://demo.ziti.dev/edge/management/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ztSession
configuration.api_key['ztSession'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = terminator_api.TerminatorApi(api_client)
    id = "id_example" # str | The id of the requested resource

    # example passing only required values which don't have defaults set
    try:
        # Retrieves a single terminator
        api_response = api_instance.detail_terminator(id)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling TerminatorApi->detail_terminator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |

### Return type

[**DetailTerminatorEnvelope**](DetailTerminatorEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single terminator |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_terminators**
> ListTerminatorsEnvelope list_terminators()

List terminators

Retrieves a list of terminator resources; supports filtering, sorting, and pagination. Requires admin access. 

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import terminator_api
from openziti_edge_management.model.list_terminators_envelope import ListTerminatorsEnvelope
from openziti_edge_management.model.api_error_envelope import ApiErrorEnvelope
from pprint import pprint
# Defining the host is optional and defaults to https://demo.ziti.dev/edge/management/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_management.Configuration(
    host = "https://demo.ziti.dev/edge/management/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ztSession
configuration.api_key['ztSession'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = terminator_api.TerminatorApi(api_client)
    limit = 1 # int |  (optional)
    offset = 1 # int |  (optional)
    filter = "filter_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List terminators
        api_response = api_instance.list_terminators(limit=limit, offset=offset, filter=filter)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling TerminatorApi->list_terminators: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional]
 **offset** | **int**|  | [optional]
 **filter** | **str**|  | [optional]

### Return type

[**ListTerminatorsEnvelope**](ListTerminatorsEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of terminators |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_terminator**
> Empty patch_terminator(id, terminator)

Update the supplied fields on a terminator

Update the supplied fields on a terminator. Requires admin access.

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import terminator_api
from openziti_edge_management.model.terminator_patch import TerminatorPatch
from openziti_edge_management.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_management.model.empty import Empty
from pprint import pprint
# Defining the host is optional and defaults to https://demo.ziti.dev/edge/management/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_management.Configuration(
    host = "https://demo.ziti.dev/edge/management/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ztSession
configuration.api_key['ztSession'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = terminator_api.TerminatorApi(api_client)
    id = "id_example" # str | The id of the requested resource
    terminator = TerminatorPatch(
        address="address_example",
        binding="binding_example",
        cost=TerminatorCost(0),
        precedence=TerminatorPrecedence("default"),
        router="router_example",
        service="service_example",
        tags=Tags(None),
    ) # TerminatorPatch | A terminator patch object

    # example passing only required values which don't have defaults set
    try:
        # Update the supplied fields on a terminator
        api_response = api_instance.patch_terminator(id, terminator)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling TerminatorApi->patch_terminator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |
 **terminator** | [**TerminatorPatch**](TerminatorPatch.md)| A terminator patch object |

### Return type

[**Empty**](Empty.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The patch request was successful and the resource has been altered |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_terminator**
> Empty update_terminator(id, terminator)

Update all fields on a terminator

Update all fields on a terminator by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import terminator_api
from openziti_edge_management.model.terminator_update import TerminatorUpdate
from openziti_edge_management.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_management.model.empty import Empty
from pprint import pprint
# Defining the host is optional and defaults to https://demo.ziti.dev/edge/management/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_management.Configuration(
    host = "https://demo.ziti.dev/edge/management/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ztSession
configuration.api_key['ztSession'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

# Enter a context with an instance of the API client
with openziti_edge_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = terminator_api.TerminatorApi(api_client)
    id = "id_example" # str | The id of the requested resource
    terminator = TerminatorUpdate(
        address="address_example",
        binding="binding_example",
        cost=TerminatorCost(0),
        precedence=TerminatorPrecedence("default"),
        router="router_example",
        service="service_example",
        tags=Tags(None),
    ) # TerminatorUpdate | A terminator update object

    # example passing only required values which don't have defaults set
    try:
        # Update all fields on a terminator
        api_response = api_instance.update_terminator(id, terminator)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling TerminatorApi->update_terminator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |
 **terminator** | [**TerminatorUpdate**](TerminatorUpdate.md)| A terminator update object |

### Return type

[**Empty**](Empty.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The update request was successful and the resource has been altered |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

