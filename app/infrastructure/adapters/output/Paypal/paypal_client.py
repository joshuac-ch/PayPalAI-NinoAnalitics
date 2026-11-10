# Cliente compartido
import os
import httpx
import time
from dotenv import load_dotenv
load_dotenv()

class PaypalClient:

    def __init__(self):
        self.base_url=os.getenv("PAYPAL_BASE_URL")
        self.client_id=os.getenv("PAYPAL_CLIENT_ID")
        self.client_secret=os.getenv("PAYPAL_CLIENT_SECRET")

        self.http=httpx.AsyncClient(
            base_url=self.base_url,
            timeout=20.0
        )

        self.access_token=None
        self.token_experies_at=0


    async def get_access_token(self):
        if self.access_token and time.monotonic() < self.token_expires_at:
            return self.access_token

        if not self.client_id or not self.client_secret:
            raise ValueError("Faltan las credenciales de PayPal")

        response = await self.http.post(
            "/v1/oauth2/token",
            auth=httpx.BasicAuth(
                self.client_id.strip(),
                self.client_secret.strip()
            ),
            headers={
                "Accept": "application/json",
                "Accept-Language": "en_US"
            },
            data={
                "grant_type": "client_credentials"
            }
        )

        if response.is_error:
            try:
                error_data = response.json()
            except ValueError:
                error_data = response.text

            raise RuntimeError(
                f"PayPal OAuth Error {response.status_code}: {error_data}"
            )

        data = response.json()

        self.access_token = data["access_token"]
        self.token_expires_at = (
            time.monotonic() + data["expires_in"] - 60
        )

        return self.access_token

    async def request(self,method:str,endpoint:str,**kwargs):
        token=await self.get_access_token()

        headers=kwargs.pop("headers",{})

        headers['Authorization']=f"Bearer {token}"
        headers["Content-Type"]="application/json"

        response= await self.http.request(
            method,endpoint,headers=headers,**kwargs
        )

        if response.status_code=="204":
            return None

        return response.json()

    async def close(self):
        await self.http.aclose()