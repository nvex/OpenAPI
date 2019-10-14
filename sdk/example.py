import time
import broker

from broker.client import BrokerClient

if __name__ == '__main__':

    proxies = {
        "http": "",
        "https": "",
    }

    entry_point = 'https://api.nvexchange.io/openapi'  # enter your open api entry point

    api_key = '9RYkmuk0aNc5ZI3zpPzm6IRWhpO85bcjUwfxzObUNLKCJy1w70WAcMgfh86Bjkni'
    secret = 'cZMNFI2WYNdZNm6O8rDhzhKITf9JxlCH8h2GiVGIRv016fWd08ZLY0XDeIwee8NN'

    b = BrokerClient(api_key=api_key, secret=secret, entry_point=entry_point, proxies=proxies)

    print(b.time())

    print(int(time.time() * 1000))

    # print(b.broker_info())

    # print(b.depth('BTCUSDT'))

    # print(b.trades('BTCUSDT'))

    # print(b.klines('BTCUSDT'))

    # print(b.ticker_24hr('BTCUSDT'))

    result = b.order_new(symbol='BTCUSDT', side='BUY', type='LIMIT', quantity='10', price='0.1', timeInForce='GTC')

    print(result)

    # order_id = result['orderId']

    # print(order_id)

    # print(b.order_get(order_id=order_id))

    # print(b.order_cancel(order_id=order_id))

    # print(b.open_orders())

    # print(b.history_orders())

    # print(b.account())

    # print(b.my_trades())

    # listen_key = b.stream_get_listen_key()

    # print(listen_key)

    # print(b.stream_keepalive(listen_key.get('listenKey')))

    # print(b.stream_close(listen_key.get('listenKey')))

    # print(b.deposit_orders())
