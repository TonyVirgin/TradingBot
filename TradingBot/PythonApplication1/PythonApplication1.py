import alpaca_trade_api as tradeapi

class PythonBot:
    def _int_(self):
        self.alpaca = tradeapi.rest(APCA_API_KEY_ID, APCA_API_SECRET_KEY, APCA_API_BASE_URL, api_version='v2')

    def run(self) :
        #each minute
        async def on_minute(conn, channel, bar):
            if bar.close >= bar.open and bar.open - bar.low > 0.1:
                print("Buying stock")
                self.alpaca.submit_order("MSFT", 1, 'buy', 'market', 'day')
                # take profit here
            if bar.close <= bar.open and bar.open - bar.low > 0.1:
                print("Selling")
                self.alpaca.submit_order("MSFT", 1, 'sell', 'market', 'day')

bd = PythonBot()
bd.run()
