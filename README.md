# Boomtown Cloud SDK for PYTHON (v1)

## Overview
This repository contains the open source PYTHON SDK that allows you to access the Cloud API from your PHP app.
Authentication uses a pre-shared key and secret, which is generated in our Admin Portal.

## Getting Started
To get started, clone this repository
```sh
python setup.py install
```

## API Key Generation
 - Log onto the Admin Portal (https://admin.goboomtown.com)
 - Click Providers in the left menu
 - Find your provider in the list
 - Double click your provider
 - Click API Settings, near the button of the configuration panel
 - Select Sandbox or Live, depending on the state of development
 - Click Re-Generate
 - Copy the access token and private-key, as provided in the pop-up dialog
 
## Documentation For Authorization
The Cloud API uses a keyed-HMAC (Hash Message Authentication Code) for authentication. To authenticate a request, your public (your token) & private (your secret) key are used to calculate the HMAC from a *"canonicalized resource"* based on specific elements of your request URL. Informally, we call this process "signing the request," and we call the output of the HMAC algorithm the signature.

#### **Note:**
- HMAC is based on SHA256 hashing.
- Each request will be valid for 10 seconds from when the request is signed.

#### The Canonicalized Resource Parts:
The "canonicalized resource" is comprised of the **PATH**, **QUERY** and a  **TIMESTAMP** in ISO-8601 form and will be constructed as follows in the order listed.

1. **PATH**: The URL without the hostname and **QUERY** - "/api/v2/issues"
2. **QUERY**: Anything after the **PATH**  - "?id=SOME_ID#FOO"
3. **TIMESTAMP** Date & Time in ISO8601 format - "2016-03-01T23:22:57+00:00"

###### Concatenating the **Canonicalized Resource** Parts:
- Resource Template = **PATH** + **QUERY** + : + **TIMESTAMP**
- Resource (With Query) = "/api/v2/issues?id=SOME_ID#FOO:2016-03-01T23:22:57+00:00"
- Resource (Without Query) = "/api/v2/issues:2016-03-01T23:22:57+00:00"

###### X-Boomtown-Date
- **Type**: API key 
- **API key parameter name**: X-Boomtown-Date
- **Location**: HTTP header
- **Description**: Will contain the current date+time in ISO8601 format

###### X-Boomtown-Token
- **Type**: API key 
- **API key parameter name**: X-Boomtown-Token
- **Location**: HTTP header
- **Description**:  Will contain your token/public key

###### X-Boomtown-Signature
- **Type**: API key 
- **API key parameter name**: X-Boomtown-Signature
- **Location**: HTTP header
- **Description**: Will contain the signature generated from the **Canonicalized Resource**

## Usage

#### Getting started, accessing basic data.

```python
import sys

from BoomtownClient import ApiClient
from BoomtownClient import ProvidersApi
from BoomtownClient import MerchantsApi
from BoomtownClient import IssuesApi
from BoomtownClient.rest import ApiException

# Initialize the ApiClient
apiClient = ApiClient()

# Set your API credentials
apiClient.set_api_token('YOUR_BOOMTOWN_TOKEN)
apiClient.set_api_secret(YOUR_BOOMTOWN_SECRET)

# Instantiate the ProvidersApi
# **Note:** we need to provide the API ApiClient we configured above.
providerApi = ProvidersApi(apiClient)
try:
    # Request your Provider profile
    # Note: Results are always an array of 0 or more models
    # If you just want to get right at the data call the getResults method.
    provider = providerApi.get_provider().results[0]
    print provider

    # Request your default team
    default_team = providerApi.get_provider_team(provider.default_partners_teams_id).results[0]
    print default_team

    # Get the raw response for the provider teams request and print the raw results
    team_collection = providerApi.get_provider_teams()
    print team_collection

    # Get all of the your Merchants
    member_collection = providerApi.get_provider_members().results
    print member_collection

except ApiException as e:
    print e
except:
    print "Unexpected error:", sys.exc_info()
    raise
```

#### Working with Merchant Issues
```python
# Instantiate the IssuesApi
# **Note:** we can reuse the ApiClient object created previously/above.
issuesApi = IssuesApi(apiClient)
try:
    # Get a collection of all the Issues you are managing
    # Result pagination defaults to a limit of 10 and starts from 0 if not provided
    issue_collection = issuesApi.get_issues(**{'limit': 5, 'start': 0}).results
    print issue_collection

    # Get a collection of Issues for a Merchant
    merchant_id = 'WA3QMJ'
    issue_collection = issuesApi.get_issues(**{'members_id': merchant_id}).results

    # Get a collection of all of the Issues for a Merchants User
    user_id = 'WA3QMJ-5XK'
    issue_collection = issuesApi.get_issues(**{'members_users_id': user_id}).results

    # Get a collection of Issues for a Merchants Location
    location_id = 'WA3QMJ-FYH'
    issue_collection = issuesApi.get_issues(**{'members_locations_id': location_id}).results

    # Lets grab the first issue and do a few things with it
    issue = issue_collection[0]

    # Lets log a note against this Issue
    issuesApi.create_issue_log(issue.id, 'Hi, this is a note')

    # Lets advance the Issues status to "Resolved"
    issuesApi.resolve_issue(issue.id)

    # Finally lets cancel the Issue
    issuesApi.cancel_issue(issue.id)

except ApiException as e:
    print e
except:
    print "Unexpected error:", sys.exc_info()
    raise
```

#### Creating a new Merchant and creating a new Issue for them
```python
from BoomtownClient.models import Issue
from BoomtownClient.models import Member
from BoomtownClient.models import MemberUser
from BoomtownClient.models import MemberLocation
from BoomtownClient.models import MemberCreateRequest

merchantApi = MerchantsApi(apiClient)
issuesApi = IssuesApi(apiClient)
try:
    # First Lets create a new Merchant,
    # we will simultaneously create a user and a location
    new_merchant_data = MemberCreateRequest()

    # Create the member
    members = Member()
    members.name = 'A Merchant'
    members.city = 'San Francisco'
    members.state = 'CA'
    members.zipcode = '94101'
    members.email = 'info@aMerchant.com'
    members.phone = '555 555 5555'
    members.street_1 = '123 Sky Lane'
    new_merchant_data.members = members

    # Create the User
    user = MemberUser()
    user.first_name = 'Bob'
    user.last_name = 'Mango'
    user.email = 'bmango@aMerchant.com'
    user.sms_number = '999 999 9999'
    new_merchant_data.members_users = user

    # Create the Location
    location = MemberLocation()
    location.site_name = 'A Merchants Mango'
    location.city = 'San Francisco'
    location.state = 'CA'
    location.zipcode = '94101'
    location.street_1 = '1 Mango Lofts'
    location.street_2 = '#1337'
    new_merchant_data._members_locations = location

    # Ok, lets save everything
    new_merchant = merchantApi.create_member(new_merchant_data).results
    print new_merchant

    # Now use the new Merchant data to create a Issue
    new_issue = Issue()
    new_issue.members_id = new_merchant.member.id
    new_issue.members_users_id = new_merchant.member_user.id
    new_issue.members_locations_id = new_merchant.member_location.id
    new_issue.details = 'WiFi at the speed of light please'
    new_issue.type = 'Support'

    new_issue = issuesApi.create_issue(**{'issues': new_issue})
    print new_issue

except ApiException as e:
    print e
except:
    print "Unexpected error:", sys.exc_info()
    raise
```

Cloud API documentation available at: [http://developers.goboomtown.com/](http://developers.goboomtown.com/)


## License

Please see the [license file](https://github.com/goboomtown/cloud-sdk-php/blob/master/LICENSE) for more information.