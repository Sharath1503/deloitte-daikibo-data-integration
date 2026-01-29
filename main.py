from datetime import datetime

def convert_iso_to_milliseconds(iso_time: str) -> int:
    """
    Converts ISO 8601 timestamp to milliseconds since epoch.
    Cross-platform safe (Windows & Linux).
    """
    dt = datetime.fromisoformat(iso_time.replace("Z", "+00:00"))
    return int(dt.timestamp() * 1000)


def unify_telemetry(format1_data, format2_data):
    """
    Unifies two telemetry formats into a single standard structure.
    """
    unified = []

    # Format 1 already uses milliseconds
    for item in format1_data:
        unified.append({
            "deviceId": item["deviceId"],
            "timestamp": item["timestamp"],
            "temperature": item["temperature"],
            "pressure": item["pressure"]
        })

    # Format 2 uses ISO timestamps
    for item in format2_data:
        unified.append({
            "deviceId": item["device"],
            "timestamp": convert_iso_to_milliseconds(item["time"]),
            "temperature": item["temp"],
            "pressure": item["pressure"]
        })

    return unified


if __name__ == "__main__":
    print("Telemetry data unification logic implemented.")
