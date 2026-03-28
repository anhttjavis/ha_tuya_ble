import sys
import os

# Xóa thư mục hiện tại khỏi vị trí ưu tiên đầu danh sách path để tránh Python import nhầm file select.py của Home Assistant 
script_dir = os.path.dirname(os.path.abspath(__file__))
if sys.path[0] == script_dir or sys.path[0] == '':
    sys.path.pop(0)

# Chèn lại xuống cuối danh sách để vẫn có thể import thư viện tuya_ble
sys.path.append(script_dir)

import asyncio
from bleak import BleakScanner
from tuya_ble.tuya_ble import TuyaBLEDevice
from tuya_ble.manager import AbstaractTuyaBLEDeviceManager, TuyaBLEDeviceCredentials

class SimpleTuyaManager(AbstaractTuyaBLEDeviceManager):
    async def get_device_credentials(self, address: str, force_update: bool = False, save_data: bool = False) -> TuyaBLEDeviceCredentials | None:
        return TuyaBLEDeviceCredentials(
            uuid="0629360870dde193",   
            local_key="g>})`+tKG^!pb2k&", 
            device_id="eb90a6f54p5umfue", 
            category="jtmspro", # Mã ngành mẫu (thường khoá là jtmspro, ms, v.v...)                 
            product_id="5ufgvhen",
            device_name="Test Smart Lock",
            product_model="Mosp800\u5145\u7535\u6b3e\uff0c58c6_7352_spt\u5355\u7ebf\u4e32\u53e3\u706f\u63a7del",
            product_name="SP800"
        )

def on_state_changed(datapoints):
    """Callback được gọi mỗi khi có dữ liệu trạng thái mới gửi từ khoá."""
    print("\n[!] --- NHẬN ĐƯỢC CẬP NHẬT TRẠNG THÁI ---")
    for dp in datapoints:
        print(f" Datapoint ID: {dp.id}")
        print(f"   Loại Data : {dp.type.name}")
        print(f"   Giá trị   : {dp.value}")
    print("----------------------------------------\n")

async def main():
    mac_address = "DC:23:52:E7:F6:45"  # Thay bằng MAC address của khoá
    
    print(f"Đang dò tìm thiết bị {mac_address}...")
    ble_device = await BleakScanner.find_device_by_address(mac_address, timeout=10.0)
    
    if not ble_device:
        print("Không tìm thấy thiết bị, vui lòng kiểm tra lại MAC.")
        return
        
    print("Đã tìm thấy khoá, khởi tạo controller...")
    manager = SimpleTuyaManager()
    tuya_device = TuyaBLEDevice(manager, ble_device)
    
    # Đăng ký hàm callback lắng nghe trạng thái (GATT Notify)
    unregister = tuya_device.register_callback(on_state_changed)
    
    # Load thông tin mã xác thực
    await tuya_device.initialize()
    
    print("Bắt đầu kết nối tới khoá và yêu cầu đồng bộ trạng thái...")
    try:
        # Hàm update() sẽ kích hoạt kết nối, pair và gửi mã yêu cầu khoá sync toàn bộ trạng thái hiện tại (FUN_SENDER_DEVICE_STATUS)
        await tuya_device.update()
        
        print("Đang lắng nghe... Hãy thử thao tác mở khoá hoặc vặn chốt trên thiết bị thực tế.")
        # Giữ chương trình chạy vô thời hạn để liên tục nhận tín hiệu Notify từ khoá
        while True:
            await asyncio.sleep(1)
            
    except KeyboardInterrupt:
        print("Dừng chương trình.")
    finally:
        # Huỷ đăng ký và ngắt kết nối an toàn khi tắt tool
        unregister()
        await tuya_device.stop()
        print("Đã ngắt kết nối.")

if __name__ == "__main__":
    asyncio.run(main())

