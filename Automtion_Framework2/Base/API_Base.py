import requests
import json
import logging

class APIBase:
    def __init__(self):
        self.log=logging.getLogger(__name__)
    def get_method(self,url,header=None,playload=None):
        header=header if header else {}
        playload=playload if playload else {}
        self.log.info(f"url:{url}")
        self.log.info(f"Header:{header}")
        self.log.info(f"playload:{playload}")
        response=requests.request("GET",url,headers=header,data=playload)
        self.log.info(f"response content :{response.text}")
        self.log.info(f"status:{response.status_code}")
        return response.json(),response.status_code

    def post_method(self,url,header=None,playload=None):
        header=header if header else {}
        playload=playload if playload else {}
        self.log.info(f"url:{url}")
        self.log.info(f"Header:{header}")
        self.log.info(f"playload:{playload}")
        response=requests.request("POST",url,headers=header,data=playload)
        self.log.info(f"response content :{response.text}")
        self.log.info(f"status:{response.status_code}")
        return response.json(),response.status_code

    def put_method(self,url,header=None,playload=None):
        header=header if header else {}
        playload=playload if playload else {}
        self.log.info(f"url:{url}")
        self.log.info(f"Header:{header}")
        self.log.info(f"playload:{playload}")
        response=requests.request("PUT",url,headers=header,data=playload)
        self.log.info(f"response content :{response.text}")
        self.log.info(f"status:{response.status_code}")
        return response.json(),response.status_code

    def patch_method(self,url,header=None,playload=None):
        header=header if header else {}
        playload=playload if playload else {}
        self.log.info(f"url:{url}")
        self.log.info(f"Header:{header}")
        self.log.info(f"playload:{playload}")
        response=requests.request("PATCH",url,headers=header,data=playload)
        self.log.info(f"response content :{response.text}")
        self.log.info(f"status:{response.status_code}")
        return response.json(),response.status_code

    def delete_method(self,url,header=None,playload=None):
        header=header if header else {}
        playload=playload if playload else {}
        self.log.info(f"url:{url}")
        self.log.info(f"Header:{header}")
        self.log.info(f"playload:{playload}")
        response=requests.request("DELETE",url,headers=header,data=playload)
        self.log.info(f"response content :{response.text}")
        self.log.info(f"status:{response.status_code}")
        return response.json(),response.status_code


