from .Coincatch_Futures import CoinexFutures

API_KEY = 'YOUR_API_KEY'
SECRET_KEY = 'YOUR_SECRET_KEY'
PASSPHRASE = 'YOUR_PASSPHRASE'
coincatch = CoinCatchFutures( API_KEY, SECRET_KEY, PASSPHRASE)


# Example Usage
if __name__ == "__main__":
    print(coincatch.get_balance())

    print("open  all position:", coincatch.get_all_positions())

    print('close position:', coincatch.close_position('BTCUSDT_UMCBL','long'))

    print("Placing Order:", coincatch.place_order('BTCUSDT_UMCBL', size=0.001, side='open_long'))

    print("Open Position symbol:", coincatch.get_open_position_symbol('BTCUSDT_UMCBL'))

    print("Change Leverage:", coincatch.change_leverage('BTCUSDT_UMCBL', 100))

    print("get all symbol:", coincatch.get_all_symbols())

    print("get_merged_depth_data:", coincatch.get_merged_depth_data('BTCUSDT_UMCBL'))

    print("ticker:", coincatch.get_ticker('BTCUSDT_UMCBL'))

    print("ticker:", coincatch.get_all_ticker())
    
    print("get_fill_detail:", coincatch.get_fill_detail('BTCUSDT_UMCBL'))

    print("open orders:", coincatch.get_open_order('BTCUSDT_UMCBL'))

    print("open  all orders:", coincatch.get_all_open_order())
    
    print("Contract Depth:", coincatch.get_contract_depth('BTCUSDT_UMCBL'))
