import asyncio
import bleak

async def scan_for_ble_devices():
    try:
        devices = await bleak.discover()
        if devices:
            print("Discovered BLE device(s):")
            for device in devices:
                print(f"Device name: {device.name}, Address: {device.address}")
                if device.metadata:
                    manufacturer_data = device.metadata.get("manufacturer_data")
                    if manufacturer_data:
                        # Extract and print manufacturer codes
                        for manufacturer_code, data in manufacturer_data.items():
                            hex_manufacturer_code = ''.join(f'{byte:02X}' for byte in manufacturer_data)
                            hex_data = ''.join(f'{byte:02X}' for byte in data)
                            print(f"Manufacturer 0x{hex_manufacturer_code}\nData 0x{hex_data}")
                    else:
                        print("No manufacturer data set")
                print()
        else:
            print("No BLE devices found nearby.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(scan_for_ble_devices())
