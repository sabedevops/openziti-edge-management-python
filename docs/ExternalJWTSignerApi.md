# openziti_edge_management.ExternalJWTSignerApi

All URIs are relative to *https://demo.ziti.dev/edge/management/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_external_jwt_signer**](ExternalJWTSignerApi.md#create_external_jwt_signer) | **POST** /external-jwt-signers | Creates an External JWT Signer
[**delete_external_jwt_signer**](ExternalJWTSignerApi.md#delete_external_jwt_signer) | **DELETE** /external-jwt-signers/{id} | Delete an External JWT Signer
[**detail_external_jwt_signer**](ExternalJWTSignerApi.md#detail_external_jwt_signer) | **GET** /external-jwt-signers/{id} | Retrieves a single External JWT Signer
[**list_external_jwt_signers**](ExternalJWTSignerApi.md#list_external_jwt_signers) | **GET** /external-jwt-signers | List External JWT Signers
[**patch_external_jwt_signer**](ExternalJWTSignerApi.md#patch_external_jwt_signer) | **PATCH** /external-jwt-signers/{id} | Update the supplied fields on an External JWT Signer
[**update_external_jwt_signer**](ExternalJWTSignerApi.md#update_external_jwt_signer) | **PUT** /external-jwt-signers/{id} | Update all fields on an External JWT Signer


# **create_external_jwt_signer**
> CreateEnvelope create_external_jwt_signer(external_jwt_signer)

Creates an External JWT Signer

Creates an External JWT Signer. Requires admin access.

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import external_jwt_signer_api
from openziti_edge_management.model.create_envelope import CreateEnvelope
from openziti_edge_management.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_management.model.external_jwt_signer_create import ExternalJwtSignerCreate
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
    api_instance = external_jwt_signer_api.ExternalJWTSignerApi(api_client)
    external_jwt_signer = ExternalJwtSignerCreate(
        audience="audience_example",
        cert_pem="cert_pem_example",
        claims_property="claims_property_example",
        enabled=True,
        external_auth_url="external_auth_url_example",
        issuer="issuer_example",
        jwks_endpoint="jwks_endpoint_example",
        kid="kid_example",
        name="MyApps Signer",
        tags=Tags(None),
        use_external_id=True,
    ) # ExternalJwtSignerCreate | An External JWT Signer to create

    # example passing only required values which don't have defaults set
    try:
        # Creates an External JWT Signer
        api_response = api_instance.create_external_jwt_signer(external_jwt_signer)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling ExternalJWTSignerApi->create_external_jwt_signer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_jwt_signer** | [**ExternalJwtSignerCreate**](ExternalJwtSignerCreate.md)| An External JWT Signer to create |

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

# **delete_external_jwt_signer**
> Empty delete_external_jwt_signer(id)

Delete an External JWT Signer

Delete an External JWT Signer by id. Requires admin access. 

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import external_jwt_signer_api
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
    api_instance = external_jwt_signer_api.ExternalJWTSignerApi(api_client)
    id = "id_example" # str | The id of the requested resource

    # example passing only required values which don't have defaults set
    try:
        # Delete an External JWT Signer
        api_response = api_instance.delete_external_jwt_signer(id)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling ExternalJWTSignerApi->delete_external_jwt_signer: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detail_external_jwt_signer**
> DetailExternalJwtSignerEnvelope detail_external_jwt_signer(id)

Retrieves a single External JWT Signer

Retrieves a single External JWT Signer by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import external_jwt_signer_api
from openziti_edge_management.model.detail_external_jwt_signer_envelope import DetailExternalJwtSignerEnvelope
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
    api_instance = external_jwt_signer_api.ExternalJWTSignerApi(api_client)
    id = "id_example" # str | The id of the requested resource

    # example passing only required values which don't have defaults set
    try:
        # Retrieves a single External JWT Signer
        api_response = api_instance.detail_external_jwt_signer(id)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling ExternalJWTSignerApi->detail_external_jwt_signer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |

### Return type

[**DetailExternalJwtSignerEnvelope**](DetailExternalJwtSignerEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A singular External JWT Signer resource |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_external_jwt_signers**
> ListExternalJwtSignersEnvelope list_external_jwt_signers()

List External JWT Signers

Retrieves a list of external JWT signers for authentication

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import external_jwt_signer_api
from openziti_edge_management.model.list_external_jwt_signers_envelope import ListExternalJwtSignersEnvelope
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
    api_instance = external_jwt_signer_api.ExternalJWTSignerApi(api_client)
    limit = 1 # int |  (optional)
    offset = 1 # int |  (optional)
    filter = "filter_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List External JWT Signers
        api_response = api_instance.list_external_jwt_signers(limit=limit, offset=offset, filter=filter)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling ExternalJWTSignerApi->list_external_jwt_signers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional]
 **offset** | **int**|  | [optional]
 **filter** | **str**|  | [optional]

### Return type

[**ListExternalJwtSignersEnvelope**](ListExternalJwtSignersEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of External JWT Signers |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_external_jwt_signer**
> Empty patch_external_jwt_signer(id, external_jwt_signer)

Update the supplied fields on an External JWT Signer

Update only the supplied fields on an External JWT Signer by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import external_jwt_signer_api
from openziti_edge_management.model.external_jwt_signer_patch import ExternalJwtSignerPatch
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
    api_instance = external_jwt_signer_api.ExternalJWTSignerApi(api_client)
    id = "id_example" # str | The id of the requested resource
    external_jwt_signer = ExternalJwtSignerPatch(
        audience="audience_example",
        cert_pem="cert_pem_example",
        claims_property="claims_property_example",
        enabled=True,
        external_auth_url="external_auth_url_example",
        issuer="issuer_example",
        jwks_endpoint="jwks_endpoint_example",
        kid="kid_example",
        name="MyApps Signer",
        tags=Tags(None),
        use_external_id=True,
    ) # ExternalJwtSignerPatch | An External JWT Signer patch object

    # example passing only required values which don't have defaults set
    try:
        # Update the supplied fields on an External JWT Signer
        api_response = api_instance.patch_external_jwt_signer(id, external_jwt_signer)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling ExternalJWTSignerApi->patch_external_jwt_signer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |
 **external_jwt_signer** | [**ExternalJwtSignerPatch**](ExternalJwtSignerPatch.md)| An External JWT Signer patch object |

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

# **update_external_jwt_signer**
> Empty update_external_jwt_signer(id, external_jwt_signer)

Update all fields on an External JWT Signer

Update all fields on an External JWT Signer by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import external_jwt_signer_api
from openziti_edge_management.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_management.model.empty import Empty
from openziti_edge_management.model.external_jwt_signer_update import ExternalJwtSignerUpdate
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
    api_instance = external_jwt_signer_api.ExternalJWTSignerApi(api_client)
    id = "id_example" # str | The id of the requested resource
    external_jwt_signer = ExternalJwtSignerUpdate(
        audience="audience_example",
        cert_pem="cert_pem_example",
        claims_property="claims_property_example",
        enabled=True,
        external_auth_url="external_auth_url_example",
        issuer="issuer_example",
        jwks_endpoint="jwks_endpoint_example",
        kid="kid_example",
        name="MyApps Signer",
        tags=Tags(None),
        use_external_id=True,
    ) # ExternalJwtSignerUpdate | An External JWT Signer update object

    # example passing only required values which don't have defaults set
    try:
        # Update all fields on an External JWT Signer
        api_response = api_instance.update_external_jwt_signer(id, external_jwt_signer)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling ExternalJWTSignerApi->update_external_jwt_signer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |
 **external_jwt_signer** | [**ExternalJwtSignerUpdate**](ExternalJwtSignerUpdate.md)| An External JWT Signer update object |

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

