#### Diagram Boto3 and Botocore


##### Boto3
    
    Session
    Config
    Resources
    ->high level interface to aws
    
    Clients
    ->Low level interface to AWS
    methods map close to 1:1, with service APIs.
    
    
##### Botocore

    Session
    Credentials
    
    Clients: HTTP, 
    Authentication, Serialization

#### Diff between clients and resources.

    Clients:
    
    exposes botocore clients to developers
    generated from JSON service descriptions
    provides low-level access
    Typicaly maps 1:1 with the service API.
    ListBuckets -> list_buckets.
    
    ResourceS:
   
    Generated from JSON resources descriptions
    Object-oriented API
    Identifiers and attributes
    Actions
    References
    Sub-resources
    Collections
      
