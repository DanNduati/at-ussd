<h1 align="center"><b>Africa's Talking USSD</b></h1>

Processing USSD requests using the Africa’s Talking API is very easy. Once your account is set up, you will need to:

- Register a service code
- Register a callback URL that AT will call whenever a request from a client hits there system.

Once you register your callback URL, any requests AT receives belonging to your service code will trigger a HTTP POST request to the registered callback with the requests data. You can read the data from the form fields of the request. Content-Type: `application/x-www-form-urlencoded`.

## Handling Sessions
This is as easy as implementing a script on your web server that handles `HTTP POST` requests.
### Session Pointers
- USSD is session driven. Every request AT sends you will contain a sessionId, and this will be maintained until that session is completed
- You will need to let the Mobile Service Provider know whether the session is complete or not. If the session is ongoing, begin your response with CON. If this is the last response for that session, begin your response with END.
- If AT gets a HTTP error response (Code 40X) from your script, or a malformed response (does not begin with CON or END), they terminate the USSD session gracefully.
- Your USSD Menu should not contain special characters as the telcos are unable to render such content, which could lead to disruptions in accessing your USSD services.

## API parameters
The API makes a `HTTP POST` request to your server with the parameters:
- 1. `sessionId` : *String* -> A unique value generated when the session starts and sent every time a mobile subscriber response has been received.
- 2. `phoneNumber` : *String* -> The number of the mobile subscriber interacting with your ussd application.
- 3. `networkCode` : *String* -> The telco of the phoneNumber interacting with your ussd application.
- 4. `serviceCode` : *String* -> This is the USSD code assigned to your application
- 5. `text` : *String* -> This shows the user input. It is an empty string in the first notification of a session. After that, it concatenates all the user input within the session with a * until the session ends.