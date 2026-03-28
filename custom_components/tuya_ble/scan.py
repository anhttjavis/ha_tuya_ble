import sys
import os
import io

# Đảm bảo in tiếng Việt không bị lỗi font khi ghi ra log (UnicodeEncodeError)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

script_dir = os.path.dirname(os.path.abspath(__file__))
if sys.path[0] == script_dir or sys.path[0] == '':
    sys.path.pop(0)
sys.path.append(script_dir)

import asyncio
from bleak import BleakScanner

async def main():
    print("Đang quét các thiết bị Bluetooth xung quanh trong 10 giây...")
    
    # Sử dụng discover để lấy cả BLEDevice lẫn AdvertisementData (chứa thông tin RSSI)
    devices = await BleakScanner.discover(timeout=10.0, return_adv=True)
    
    print(f"\nTìm thấy {len(devices)} thiết bị. Danh sách:")
    # devices là dạng dict { MAC_Address : (BLEDevice, AdvertisementData) }
    for mac, (device_info, adv_data) in devices.items():
        name = device_info.name or "Không có tên"
        rssi = adv_data.rssi
        
        # Chỉ in các thiết bị để dễ kiểm tra
        print(f" - MAC: {mac} | Tên: {name} | RSSI: {rssi}")

if __name__ == "__main__":
    asyncio.run(main())
