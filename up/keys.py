class Keys:
    accounts = [
    {"username":"username","weight":100,"posting_key":"key"},
    ]
    keys = []
    for account in accounts:
        keys.append(account["posting_key"])
