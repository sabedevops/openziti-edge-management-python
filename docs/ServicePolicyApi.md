# openziti_edge_management.ServicePolicyApi

All URIs are relative to *https://demo.ziti.dev/edge/management/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_policy**](ServicePolicyApi.md#create_service_policy) | **POST** /service-policies | Create a service policy resource
[**delete_service_policy**](ServicePolicyApi.md#delete_service_policy) | **DELETE** /service-policies/{id} | Delete a service policy
[**detail_service_policy**](ServicePolicyApi.md#detail_service_policy) | **GET** /service-policies/{id} | Retrieves a single service policy
[**list_service_policies**](ServicePolicyApi.md#list_service_policies) | **GET** /service-policies | List service policies
[**list_service_policy_identities**](ServicePolicyApi.md#list_service_policy_identities) | **GET** /service-policies/{id}/identities | List identities a service policy affects
[**list_service_policy_posture_checks**](ServicePolicyApi.md#list_service_policy_posture_checks) | **GET** /service-policies/{id}/posture-checks | List posture check a service policy includes
[**list_service_policy_services**](ServicePolicyApi.md#list_service_policy_services) | **GET** /service-policies/{id}/services | List services a service policy affects
[**patch_service_policy**](ServicePolicyApi.md#patch_service_policy) | **PATCH** /service-policies/{id} | Update the supplied fields on a service policy
[**update_service_policy**](ServicePolicyApi.md#update_service_policy) | **PUT** /service-policies/{id} | Update all fields on a service policy


# **create_service_policy**
> CreateEnvelope create_service_policy(policy)

Create a service policy resource

Create a service policy resource. Requires admin access.

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import service_policy_api
from openziti_edge_management.model.create_envelope import CreateEnvelope
from openziti_edge_management.model.service_policy_create import ServicePolicyCreate
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
    api_instance = service_policy_api.ServicePolicyApi(api_client)
    policy = ServicePolicyCreate(
        identity_roles=Roles([
            "identity_roles_example",
        ]),
        name="name_example",
        posture_check_roles=Roles([
            "posture_check_roles_example",
        ]),
        semantic=Semantic("AllOf"),
        service_roles=Roles([
            "service_roles_example",
        ]),
        tags=Tags(None),
        type=DialBind("Dial"),
    ) # ServicePolicyCreate | A service policy to create

    # example passing only required values which don't have defaults set
    try:
        # Create a service policy resource
        api_response = api_instance.create_service_policy(policy)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling ServicePolicyApi->create_service_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy** | [**ServicePolicyCreate**](ServicePolicyCreate.md)| A service policy to create |

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

# **delete_service_policy**
> Empty delete_service_policy(id)

Delete a service policy

Delete a service policy by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import service_policy_api
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
    api_instance = service_policy_api.ServicePolicyApi(api_client)
    id = "id_example" # str | The id of the requested resource

    # example passing only required values which don't have defaults set
    try:
        # Delete a service policy
        api_response = api_instance.delete_service_policy(id)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling ServicePolicyApi->delete_service_policy: %s\n" % e)
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

# **detail_service_policy**
> DetailServicePolicyEnvelop detail_service_policy(id)

Retrieves a single service policy

Retrieves a single service policy by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import service_policy_api
from openziti_edge_management.model.detail_service_policy_envelop import DetailServicePolicyEnvelop
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
    api_instance = service_policy_api.ServicePolicyApi(api_client)
    id = "id_example" # str | The id of the requested resource

    # example passing only required values which don't have defaults set
    try:
        # Retrieves a single service policy
        api_response = api_instance.detail_service_policy(id)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling ServicePolicyApi->detail_service_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |

### Return type

[**DetailServicePolicyEnvelop**](DetailServicePolicyEnvelop.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single service policy |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_policies**
> ListServicePoliciesEnvelope list_service_policies()

List service policies

Retrieves a list of service policy resources; supports filtering, sorting, and pagination. Requires admin access. 

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import service_policy_api
from openziti_edge_management.model.list_service_policies_envelope import ListServicePoliciesEnvelope
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
    api_instance = service_policy_api.ServicePolicyApi(api_client)
    limit = 1 # int |  (optional)
    offset = 1 # int |  (optional)
    filter = "filter_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List service policies
        api_response = api_instance.list_service_policies(limit=limit, offset=offset, filter=filter)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling ServicePolicyApi->list_service_policies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional]
 **offset** | **int**|  | [optional]
 **filter** | **str**|  | [optional]

### Return type

[**ListServicePoliciesEnvelope**](ListServicePoliciesEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of service policies |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_policy_identities**
> ListIdentitiesEnvelope list_service_policy_identities(id)

List identities a service policy affects

Retrieves a list of identity resources that are affected by a service policy; supports filtering, sorting, and pagination. Requires admin access. 

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import service_policy_api
from openziti_edge_management.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_management.model.list_identities_envelope import ListIdentitiesEnvelope
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
    api_instance = service_policy_api.ServicePolicyApi(api_client)
    id = "id_example" # str | The id of the requested resource
    limit = 1 # int |  (optional)
    offset = 1 # int |  (optional)
    filter = "filter_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List identities a service policy affects
        api_response = api_instance.list_service_policy_identities(id)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling ServicePolicyApi->list_service_policy_identities: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List identities a service policy affects
        api_response = api_instance.list_service_policy_identities(id, limit=limit, offset=offset, filter=filter)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling ServicePolicyApi->list_service_policy_identities: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |
 **limit** | **int**|  | [optional]
 **offset** | **int**|  | [optional]
 **filter** | **str**|  | [optional]

### Return type

[**ListIdentitiesEnvelope**](ListIdentitiesEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of identities |  -  |
**400** | The requested resource does not exist |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_policy_posture_checks**
> ListPostureCheckEnvelope list_service_policy_posture_checks(id)

List posture check a service policy includes

Retrieves a list of posture check resources that are affected by a service policy; supports filtering, sorting, and pagination. Requires admin access. 

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import service_policy_api
from openziti_edge_management.model.list_posture_check_envelope import ListPostureCheckEnvelope
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
    api_instance = service_policy_api.ServicePolicyApi(api_client)
    id = "id_example" # str | The id of the requested resource
    limit = 1 # int |  (optional)
    offset = 1 # int |  (optional)
    filter = "filter_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List posture check a service policy includes
        api_response = api_instance.list_service_policy_posture_checks(id)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling ServicePolicyApi->list_service_policy_posture_checks: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List posture check a service policy includes
        api_response = api_instance.list_service_policy_posture_checks(id, limit=limit, offset=offset, filter=filter)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling ServicePolicyApi->list_service_policy_posture_checks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |
 **limit** | **int**|  | [optional]
 **offset** | **int**|  | [optional]
 **filter** | **str**|  | [optional]

### Return type

[**ListPostureCheckEnvelope**](ListPostureCheckEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of posture checks |  -  |
**400** | The requested resource does not exist |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_policy_services**
> ListServicesEnvelope list_service_policy_services(id)

List services a service policy affects

Retrieves a list of service resources that are affected by a service policy; supports filtering, sorting, and pagination. Requires admin access. 

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import service_policy_api
from openziti_edge_management.model.list_services_envelope import ListServicesEnvelope
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
    api_instance = service_policy_api.ServicePolicyApi(api_client)
    id = "id_example" # str | The id of the requested resource
    limit = 1 # int |  (optional)
    offset = 1 # int |  (optional)
    filter = "filter_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List services a service policy affects
        api_response = api_instance.list_service_policy_services(id)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling ServicePolicyApi->list_service_policy_services: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List services a service policy affects
        api_response = api_instance.list_service_policy_services(id, limit=limit, offset=offset, filter=filter)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling ServicePolicyApi->list_service_policy_services: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |
 **limit** | **int**|  | [optional]
 **offset** | **int**|  | [optional]
 **filter** | **str**|  | [optional]

### Return type

[**ListServicesEnvelope**](ListServicesEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of services |  -  |
**400** | The requested resource does not exist |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_service_policy**
> Empty patch_service_policy(id, policy)

Update the supplied fields on a service policy

Update the supplied fields on a service policy. Requires admin access.

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import service_policy_api
from openziti_edge_management.model.service_policy_patch import ServicePolicyPatch
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
    api_instance = service_policy_api.ServicePolicyApi(api_client)
    id = "id_example" # str | The id of the requested resource
    policy = ServicePolicyPatch(
        identity_roles=Roles([
            "identity_roles_example",
        ]),
        name="name_example",
        posture_check_roles=Roles([
            "posture_check_roles_example",
        ]),
        semantic=Semantic("AllOf"),
        service_roles=Roles([
            "service_roles_example",
        ]),
        tags=Tags(None),
        type=DialBind("Dial"),
    ) # ServicePolicyPatch | A service policy patch object

    # example passing only required values which don't have defaults set
    try:
        # Update the supplied fields on a service policy
        api_response = api_instance.patch_service_policy(id, policy)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling ServicePolicyApi->patch_service_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |
 **policy** | [**ServicePolicyPatch**](ServicePolicyPatch.md)| A service policy patch object |

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

# **update_service_policy**
> Empty update_service_policy(id, policy)

Update all fields on a service policy

Update all fields on a service policy by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_management
from openziti_edge_management.api import service_policy_api
from openziti_edge_management.model.service_policy_update import ServicePolicyUpdate
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
    api_instance = service_policy_api.ServicePolicyApi(api_client)
    id = "id_example" # str | The id of the requested resource
    policy = ServicePolicyUpdate(
        identity_roles=Roles([
            "identity_roles_example",
        ]),
        name="name_example",
        posture_check_roles=Roles([
            "posture_check_roles_example",
        ]),
        semantic=Semantic("AllOf"),
        service_roles=Roles([
            "service_roles_example",
        ]),
        tags=Tags(None),
        type=DialBind("Dial"),
    ) # ServicePolicyUpdate | A service policy update object

    # example passing only required values which don't have defaults set
    try:
        # Update all fields on a service policy
        api_response = api_instance.update_service_policy(id, policy)
        pprint(api_response)
    except openziti_edge_management.ApiException as e:
        print("Exception when calling ServicePolicyApi->update_service_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |
 **policy** | [**ServicePolicyUpdate**](ServicePolicyUpdate.md)| A service policy update object |

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

