#### Basic Auth sample proxy
This proxy enforces basic authorization.

##### How to use
1. Import or create the proxy (natch).
2. Create an app in the Edge platform.
3. Use the app's consumer key and secret as user/pass when making the http request.

##### How it works

1. Extract variables to pull out the base64 encoded auth header
2. Python policy to extract the username and password from the header
3. AccessEntity policy to look up app details based on the extracted username
4. RaiseFault policy to throw a 401 if the retrieved password (client secret) does not match the one passed in the header
