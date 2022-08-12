import applemusicpy


def search_apple(secret_key, key_id, team_id):
    am = applemusicpy.AppleMusic(secret_key=secret_key, key_id=key_id, team_id=team_id)
    results = am.search('travis scott', types=['albums'], limit=5)
    for item in results['results']['albums']['data']:
        print(item['attributes']['name'])


def call_apple():

    secret_key = "MIGTAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBHkwdwIBAQQg60ZxEmcVo16a+aH21oEiLnTxg0sjHPE6TJ820hXO6O2gCgYIKoZIzj0DAQehRANCAASpq7e4DkBLcMpUTSRjIW4WEnbJg8hjyZWnUohQnDqIEpDd+PtxNeJU+Q9jg2T34wj33YWlEQJctIdiEWuabok9"
    key_id = "M9853P5T6W"
    team_id = '9LYHZBVHB7'

    search_apple(secret_key, key_id, team_id)
