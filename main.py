import requests

direct_url = "http://magic.wizards.com/sites/all/modules/custom/wiz_services/mtgo_status.php"
backup_url = "http://www.wizards.com/Handlers/Status.ashx?service=mtgo"

urls = [direct_url, backup_url]

got_status = False
for url in urls:
    resp = requests.get(url)
    if resp.status_code == 200:
        status_hash = resp.json()
        if status_hash['status'] == "DOWN":
            print("MTGO is down...")
        else:
            print("MTGO is up! Go get those tickets!")
        got_status = True
        break

if not got_status:
    print("Was not able to get MTGO status, check your internet connection.")


