import connexion

# application instance
app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')
"""
    CRUD:
        Create => POST
        READ => GET
        UPDATE => PUT(replace)(entity not collection), PATH(partially a set of attributes)
        DELETE => DELETE

    You can perform these actions on a thing or resource.
    It’s useful to think about a resource as something a noun can be applied to: a person, an order for something, a person’s address.
    This idea of a resource lines up nicely with a URL (Unique Resource Locator).


    URL should identify a unique resource on the web, something that will work with the same thing over and over again for the same URL.
"""

"""
    rfc repository: https://tools.ietf.org/html/
    /api/people CREATE POST
    /api/people READ GET
    /api/people/<NAME> READ GET
    /api/people/<NAME> UPDATE PUT/ REPLEACE A RESOURCE ENTITY
    /api/people/<NAME> UPDATE PATCH, you only update the field you specify and leave the rest alone.
    /api/orders/<NAME> DELETE DELETE
    
    2616 Obsoleted by: 7230, 7231, 7232, 7233, 7234, 7235
    Updated by: 2817, 5785, 6266, 6585
    Network Working Group 
    
    7230:
        Hypertext Transfer Protocol (HTTP/1.1): Message Syntax and Routing 
    1.  "Message Syntax and Routing"(7230)

    2.  "Semantics and Content" [RFC7231]

    3.  "Conditional Requests" [RFC7232]

    4.  "Range Requests" [RFC7233]

    5.  "Caching" [RFC7234]

    6.  "Authentication" [RFC7235]
"""

"""
    HTTP CODES:
    - 200 OK
    - 202 (Accepted) if the action has been queued
    - 201 Created OK
    - 204 no content. suscceeded, but the client does not need to go away from its current page. Cachable by default
    
    - 406 Already exists
    - 400 Bad arguments
    - 403 not autorhorized
    - 404 does not exist
"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False, threaded=False)
