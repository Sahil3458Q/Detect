from bleak import BleakScanner
import asyncio
import subprocess



found = True
async def find(addr):
    global found
    
    while True:
        dev = await BleakScanner.discover()
        dev_list = [d.address for d in dev]
        
        if addr in dev_list and found:
            subprocess.run(["notify-send","Bluetooth","Device Found"])
            found = False
        elif addr not in dev_list and not found :
            subprocess.run(["notify-send","Bluetooth","Device Gone"])
            found =True

        await asyncio.sleep(2)

asyncio.run(find())

