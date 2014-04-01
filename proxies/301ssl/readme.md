#### Redirect http to https
This example contains a RaiseFault policy to redirect any http request to https.

##### How to use
1. Import or create the proxy (natch).
2. Hit it with curl

##### How it works

1. The RaiseFault policy is in the Proxy Preflow with a condition to execute only when the request is over http.
2. The RaiseFault policy returns a 301 response with the Location header matching the host and the complete URI of the request, but over https.


##### Example
I used the -k switch because I don't have a certificate configured for my custom domain.
```
curl -iLk http://api.lo5.at/v1/301ssl/answers?question=ultimate
HTTP/1.0 301 Moved Permanently
Content-Type: text/plain
Location: https://api.lo5.at/v1/301ssl/answers?question=ultimate
Content-Length: 14
X-Cache: MISS from 172.19.134.2
X-Cache-Lookup: MISS from 172.19.134.2:3128
Via: 1.0 172.19.134.2:3128 (squid/2.6.STABLE14)
Connection: close

HTTP/1.0 200 OK
Date: Tue, 01 04 2014 02:17:36 GMT
Content-Length: 24
Connection: close

Hello, World, securely.
```