from flask import Flask, request
app = Flask(__name__)

# dummy acc. data
accounts = {
    "A001": {
        "bill": "420"
    },
    "A002": {
        "bill": "1111"
    }
}


def process_response(resp: str):
    response: str = ""
    if len(resp) <= 1:
        if resp == "":
            response = "CON What would you want to check \n"
            response += "1. Query Bill \n"
            response += "2. Exit"
        elif resp == "1":
            response = "CON Enter Account number \n"
            response += "eg: A111"
        elif resp == "2":
            response = "END Bye!"
        else:
            response = "END Invalid choice selected!"
    else:
        # split the string and get the acc number
        _, account_number = resp.split('*')
        # check if account number is valid
        if account_number in accounts:
            response = f"END Your bill is kes {accounts[account_number]['bill']}"
        else:
            response = f"END Invalid account number: {account_number}!"

    return response


@app.route("/", methods=['POST', 'GET'])
def ussd_callback():
    session_id: str = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")
    #print(f"session_id: {session_id},service_code: {service_code},phone_number: {phone_number}")
    # process subscriber input
    return process_response(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
