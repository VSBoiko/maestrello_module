import requests


class MaestrelloBasic:
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    api = "https://pizzamaestrello.com/api.php/p/v1/"

    def __init__(self):
        pass

    def _validate(self, response, params):
        if response.status_code == 200:
            return response.json()

            # data = response.json()
            # if data.get('errors'):
            #     print("status_code", response.status_code)
            #     print("headers", self.headers)
            #     print("params", params)
            #     print("response", data)
            # else:
            #     return data

        else:
            print(response.status_code, response.text)
