import requests
with open("accounts.txt") as f:
    accounts = f.read()
    f.close()
    for account in accounts.strip().split("\n"):    
        r = requests.get(f"https://webapi.depop.com/api/v1/auth/checkusername/{account}")
        if r.status_code == 200:
            print(f"[Depop] Claimable: {account}")
            f = open(f'out.txt', "a")
            f.write(f"{account}\n")
            f.close()
        else:
            print(f"[Depop] Unclaimable: {account} | Reason: {r.json()['description']}")
