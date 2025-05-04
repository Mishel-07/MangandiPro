import requests
from typing import Union

class JustUploader:
    URL = "https://storage.mangoi.in" # v2

    def __init__(self, file_path: str):
        self.file_path = file_path
    
    def _upload(self) -> Union[str, dict]:
        data = self.file_path
        files = {"file": data}
        response = requests.post(
            f"{self.URL}/upload",
            files=files
        )

        if response.status_code == 200:
            return response.json()
        else:
            return "not found"

    def upload(self) -> str:
        response_json = self._upload() 
        if "url" in response_json:
            return response_json["url"]
        else:
            return "not found"
