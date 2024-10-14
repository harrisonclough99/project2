import time

from coinbase.websocket import WSClient
import os


def on_message(msg):
    print(msg)

def on_open():
    print("Connection opened!")

COINBASE_API_KEY = os.environ["COINBASE_API_KEY"]
COINBASE_API_SECRET = os.environ["COINBASE_API_SECRET"]

client = WSClient(api_key=COINBASE_API_KEY, api_secret=COINBASE_API_SECRET, on_message=on_message)


def client_subscribe():
    """
    open the connection and subscribe to the ticker and heartbeat channels for BTC-USD and ETH-USD
    :return:
    """
    client.open()

    client.subscribe(product_ids=["BTC-USD", "ETH-USD"], channels=["ticker", "heartbeats"])
    # wait 10 seconds
    time.sleep(5)

    # unsubscribe from the ticker channel and heartbeat channels for BTC-USD and ETH-USD, and close the connection
    client.unsubscribe(product_ids=["BTC-USD", "ETH-USD"], channels=["ticker", "heartbeats"])
    client.close()


client_subscribe()

if __name__ == "__main__":
    print("FINISHED")
