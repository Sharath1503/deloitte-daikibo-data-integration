import json
from datetime import datetime

def convert_iso_to_milliseconds(iso_time: str) -> int:
    dt = datetime.fromisoformat(iso_time.replace("Z", "+00:00"))
    return int(dt.timestamp() * 1000)

def unify_telemetry(format1_data, format2_data):
    unified = []

    for item in format1_data:
        unified.append({
            "deviceId": item["deviceId"],
            "timestamp": item["timestamp"],
            "temperature": item["temperature"],
            "pressure": item["pressure"]
        })

    for item in format2_data:
        unified.append({
            "deviceId": item["device"],
            "timestamp": convert_iso_to_milliseconds(item["time"]),
            "temperature": item["temp"],
            "pressure": item["pressure"]
        })

    return unified

if __name__ == "__main__":
    with open("data-1.json") as f1, open("data-2.json") as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

    result = unify_telemetry(data1, data2)
    print(json.dumps(result, indent=2))
