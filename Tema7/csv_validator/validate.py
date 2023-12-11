def validate_data(data):
    header,rows = data
    for r in rows:
        if len(r) != len(header):
            print(f"Row {r} has {len(r)} values, expected {len(header)}")
            return False
    return True