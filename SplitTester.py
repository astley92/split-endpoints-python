import http.client
import json

class Split_API_Request:
    def __init__(self, token, mode="sandbox"):
        self.token = token
        if mode == "sandbox":
            self.base_url = "api.sandbox.split.cash"
        elif mode == "production":
            self.base_url = "api.split.cash"
        else:
            raise Exception("Not a valid mode.")
        self.conn = http.client.HTTPSConnection(self.base_url)
        self.headers = {
                        'content-type': "application/json",
                        'accept': "application/json",
                        'authorization': "Bearer {}".format(self.token)
                        }
        self.data = None

    def execute(self, endpoint, payload=None, method="GET"):
        if payload != None:
            self.conn.request(method, endpoint, json.dumps(payload), headers=self.headers)
        else:
            self.conn.request(method, endpoint, headers=self.headers)
        res = self.conn.getresponse()
        self.data = res.read()

    def show_response(self, decode=False):
        if self.data != None:
            if decode:
                print(json.loads(self.data))
                self.data = None
            else:
                print(self.data)
                self.data = None
        else:
            print("No data. Could be due to not running execute command.")
