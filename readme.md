Authentication Methods

There are many web authentication methods and tools:

1) Username/email and password
Using classic HTTP Basic and Digest Authentication

2) API key
An opaque long string with an accompanying secret

3) OAuth2
A set of standards for authentication and authorization


4) JavaScript Web Tokens (JWT)
An encoding format containing cryptographically signed user information
In this section, I’ll review the first two methods and show you how to traditionally
implement them. But I’ll stop before filling out the API and database code. Instead,
we’ll fully implement a more modern scheme with OAuth2 and JWT.
