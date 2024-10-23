import json
import time
import requests
import hmac
import base64
import traceback


class CoinCatchFutures:
    def __init__(self, apiKey, secretKey, passphrase, tries = 10):
        self.apiKey = apiKey
        self.secret_key = secretKey
        self.tries = 10
        self.passphrase = passphrase
        self.BASE_URL = 'https://api.coincatch.com'


    def generate_signature(self,timestamp, method, request_path, body=''):
        """Generate the signature for API requests."""
        if body:
            content = f"{timestamp}{method}{request_path}{body}"
        else:
            content = f"{timestamp}{method}{request_path}"

        mac = hmac.new(bytes(SECRET_KEY, 'utf-8'), bytes(content, 'utf-8'), digestmod='sha256')
        return base64.b64encode(mac.digest()).decode()


    def get_headers(self, method, request_path, body=''):
        """Prepare headers for the API request."""
        timestamp = str(int(time.time() * 1000))  # Current time in milliseconds
        signature = self.generate_signature(timestamp, method, request_path, body)
        
        return {
            'ACCESS-KEY': self.apiKey,
            'ACCESS-SIGN': signature,
            'ACCESS-TIMESTAMP': timestamp,
            'ACCESS-PASSPHRASE': self.passphrase,
            'Content-Type': 'application/json'
        }


    def get_contract_depth(self ,symbol):
        """Get contract depth information for a specific symbol."""
        request_path = '/api/mix/v1/market/depth'
        query_string = f"symbol={symbol}&limit=20"
        tries = 0
        while tries < self.tries:
            tries += 1
            try:
                headers = self.get_headers('GET', f"{request_path}?{query_string}")
                response = requests.get(self.BASE_URL + request_path + f"?{query_string}", headers=headers)
                response = response.json()
                if response['code'] == '00000':
                    break

            except:
                traceback.print_exc()
                time.sleep(0.2)
        if response:
            return response
        

    def change_hols_mode(self,mode):
        # holdMode = single_hold or double_hold
        request_path = '/api/mix/v1/account/setPositionMode'
        query_string = f"productType=umcbl&holdMode={mode}"
        tries = 0
        while tries < self.tries:
            tries += 1
            try:
                headers = self.get_headers('POST', f"{request_path}?{query_string}")
                response = requests.get(self.BASE_URL + request_path + f"?{query_string}", headers=headers)
                response = response.json()
                if response['code'] == '00000':
                    break

            except:
                traceback.print_exc()
                time.sleep(0.2)
        if response:
            return response
        



    def get_open_order(self,symbol):
        request_path = '/api/mix/v1/order/current'
        query_string = f"symbol={symbol}"
        tries = 0
        while tries < self.tries:
            tries += 1
            try:
                headers = self.get_headers('GET', f"{request_path}?{query_string}")
                response = requests.get(self.BASE_URL + request_path + f"?{query_string}", headers=headers)
                response = response.json()
                if response['code'] == '00000':
                    break

            except:
                traceback.print_exc()
                time.sleep(0.2)
        if response:
            return response


    def get_fill_detail(self,symbol):
        request_path = '/api/mix/v1/order/fills'
        query_string = f"symbol={symbol}"
        tries = 0
        while tries < self.tries:
            tries += 1
            try:
                headers = self.get_headers('GET', f"{request_path}?{query_string}")
                response = requests.get(self.BASE_URL + request_path + f"?{query_string}", headers=headers)
                response = response.json()
                if response['code'] == '00000':
                    break

            except:
                traceback.print_exc()
                time.sleep(0.2)
        if response:
            return response
        


    def get_all_open_order(self):
        request_path = '/api/mix/v1/order/marginCoinCurrent'
        query_string = f"productType=umcbl"
        tries = 0
        while tries < self.tries:
            tries += 1
            try:
                headers = self.get_headers('GET', f"{request_path}?{query_string}")
                response = requests.get(self.BASE_URL + request_path + f"?{query_string}", headers=headers)
                response = response.json()
                if response['code'] == '00000':
                    break

            except:
                traceback.print_exc()
                time.sleep(0.2)
        if response:
            return response
        


    def get_all_positions(self):
        request_path = '/api/mix/v1/position/allPosition-v2'
        query_string = f"productType=umcbl"
        tries = 0
        while tries < self.tries:
            tries += 1
            try:
                headers = self.get_headers('GET', f"{request_path}?{query_string}")
                response = requests.get(self.BASE_URL + request_path + f"?{query_string}", headers=headers)
                response = response.json()
                if response['code'] == '00000':
                    break

            except:
                traceback.print_exc()
                time.sleep(0.2)
        if response:
            return response



    def get_balance(self):
        request_path = '/api/mix/v1/account/accounts'
        query_string = f"productType=umcbl"
        tries = 0
        while tries < self.tries:
            tries += 1
            try:
                headers = self.get_headers('GET', f"{request_path}?{query_string}")
                response = requests.get(self.BASE_URL + request_path + f"?{query_string}", headers=headers)
                response = response.json()
                if response['code'] == '00000':
                    break

            except:
                traceback.print_exc()
                time.sleep(0.2)
        if response:
            return response
        
        


    def get_open_position_symbol(self,symbol):
        request_path = '/api/mix/v1/position/singlePosition-v2'
        query_string = f"symbol={symbol}&marginCoin=USDT"
        tries = 0
        while tries < self.tries:
            tries += 1
            try:
                headers = self.get_headers('GET', f"{request_path}?{query_string}")
                response = requests.get(self.BASE_URL + request_path + f"?{query_string}", headers=headers)
                response = response.json()
                if response['code'] == '00000':
                    break

            except:
                traceback.print_exc()
                time.sleep(0.2)
        if response:
            return response
        


    def change_leverage(self,symbol, leverage):
        request_path = '/api/mix/v1/account/setLeverage'
        order_data = {
            "symbol": symbol,
            'marginCoin': 'USDT',
            "leverage": leverage
        }
        tries = 0
        while tries < self.tries:
            tries += 1
            try:
                body = json.dumps(order_data)
                headers = self.get_headers('POST', request_path, body)
                response = requests.post(self.BASE_URL + request_path, headers=headers, data=body)
                response = response.json()
                if response['code'] == '00000':
                    break

            except:
                traceback.print_exc()
                time.sleep(0.2)
        if response:
            return response
        


    def change_margin_mode(self,symbol, mode):
        # mode = fixed or crossed
        request_path = '/api/mix/v1/account/setMarginMode'
        order_data = {
            "symbol": symbol,
            'marginCoin': 'USDT',
            "marginMode": mode
        }
        tries = 0
        while tries < self.tries:
            tries += 1
            try:
                body = json.dumps(order_data)
                headers = self.get_headers('POST', request_path, body)
                response = requests.post(self.BASE_URL + request_path, headers=headers, data=body)
                response = response.json()
                if response['code'] == '00000':
                    break

            except:
                traceback.print_exc()
                time.sleep(0.2)
        if response:
            return response



    def change_marjin(self,symbol, amount):
        request_path = '/api/mix/v1/account/setMargin'
        order_data = {
            "symbol": symbol,
            'marginCoin': 'USDT',
            "amount": amount
        }
        tries = 0
        while tries < self.tries:
            tries += 1
            try:
                body = json.dumps(order_data)
                headers = self.get_headers('POST', request_path, body)
                response = requests.post(self.BASE_URL + request_path, headers=headers, data=body)
                response = response.json()
                if response['code'] == '00000':
                    break

            except:
                traceback.print_exc()
                time.sleep(0.2)
        if response:
            return response
        
        
    

    def place_order(self,symbol, size, side, order_type='market', price=None):
        """Place an order on the platform."""
        request_path = '/api/mix/v1/order/placeOrder'
        # Constructing the order body
        order_data = {
            "symbol": symbol,
            'marginCoin': 'USDT',
            "size": size,
            "side": side,
            "orderType": order_type
        }
        if price is not None:
            order_data["price"] = price
        tries = 0
        while tries < self.tries:
            tries += 1
            try:
                body = json.dumps(order_data)
                headers = self.get_headers('POST', request_path, body)
                response = requests.post(self.BASE_URL + request_path, headers=headers, data=body)
                response = response.json()
                if response['code'] == '00000':
                    break

            except:
                traceback.print_exc()
                time.sleep(0.2)
        if response:
            return response
        


    def get_all_symbols(self):
        request_path = '/api/mix/v1/market/contracts'
        query_string = f"productType=umcbl"
        tries = 0
        while tries < self.tries:
            tries += 1
            try:
                headers = self.get_headers('GET', f"{request_path}?{query_string}")
                response = requests.get(self.BASE_URL + request_path + f"?{query_string}", headers=headers)
                response = response.json()
                if response['code'] == '00000':
                    break

            except:
                traceback.print_exc()
                time.sleep(0.2)
        if response:
            return response
        

    def get_merged_depth_data(self,symbol):
        request_path = '/api/mix/v1/market/merge-depth'
        query_string = f"symbol={symbol}"
        tries = 0
        while tries < self.tries:
            tries += 1
            try:
                headers = self.get_headers('GET', f"{request_path}?{query_string}")
                response = requests.get(self.BASE_URL + request_path + f"?{query_string}", headers=headers)
                response = response.json()
                if response['code'] == '00000':
                    break

            except:
                traceback.print_exc()
                time.sleep(0.2)
        if response:
            return response
    

    def get_ticker(self,symbol):
        request_path = '/api/mix/v1/market/ticker'
        query_string = f"symbol={symbol}"
        tries = 0
        while tries < self.tries:
            tries += 1
            try:
                headers = self.get_headers('GET', f"{request_path}?{query_string}")
                response = requests.get(self.BASE_URL + request_path + f"?{query_string}", headers=headers)
                response = response.json()
                if response['code'] == '00000':
                    break

            except:
                traceback.print_exc()
                time.sleep(0.2)
        if response:
            return response


    def get_all_ticker(self):
        request_path = '/api/mix/v1/market/tickers'
        query_string = f"productType=umcbl"
        tries = 0
        while tries < self.tries:
            tries += 1
            try:
                headers = self.get_headers('GET', f"{request_path}?{query_string}")
                response = requests.get(self.BASE_URL + request_path + f"?{query_string}", headers=headers)
                response = response.json()
                if response['code'] == '00000':
                    break

            except:
                traceback.print_exc()
                time.sleep(0.2)
        if response:
            return response


    def close_position(self,symbol,side):
        """Close an open position."""
        tries = 0
        while tries < self.tries:
            tries += 1
            try:
                openposition = self.get_open_position_symbol(symbol)
                for i in openposition['data']:
                    if i['holdSide'] == side:
                        amount  = i['total']
                sideposition = 'close_'+side
                response = self.place_order(symbol, size=amount, side=sideposition)
                if response['code'] == '00000':
                    break

            except:
                traceback.print_exc()
                time.sleep(0.2)
        if response:
            return response
