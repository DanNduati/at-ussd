from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class UssdParams(BaseModel):
    session_id: str
    service_code: str
    phone_number: str
    text: str


# dummy acc. data
accounts = {
    "A001": {
        "bill": "420"
    },
    "A002": {
        "bill": "1111"
    }
}


async def process_response(resp: str):
    response: str = ""
    print(resp)
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


@app.get("/")
def root():
    return {"message": "Hello USSD!"}


@app.post("/callback/", response_class=HTMLResponse)
async def ussd_callback(session_id: str = Form(""), service_code: str = Form(""), phone_number: str = Form(""), text: Optional[str] = Form("")):
    # print(phone_number)
    return await process_response(text)
