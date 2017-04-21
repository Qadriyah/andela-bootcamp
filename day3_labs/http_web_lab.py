import http.client
import json

class ForeignExchangeRate():

    def __init__(self):
        self._api_address = 'api.fixer.io'

    def open_connection(self):
        try:
            http_connection = http.client.HTTPSConnection(self._api_address)
            return http_connection
        except http.client.HTTPException as err:
            print(err.args)
            return 0

    def get_latest_rates(self,
                         relative_path,
                         connection_obj):
        connection_obj.request('GET', relative_path)
        return connection_obj.getresponse()


if __name__ == '__main__':
    exchange_rate = ForeignExchangeRate()
    connection = exchange_rate.open_connection()
    if connection != 0:
        response = exchange_rate.get_latest_rates('/latest?base=USD', connection)
        if response.getcode() == 200:
            data = response.read().decode('utf8')
            data = json.loads(data)
            rates = data['rates']
            print('Base Rate: ', data['base'], '\nRates')
            for key, value in rates.items():
                print(key + ': ', value)
    else:
        print('Connection to the remote host failed')
