

import time
import urllib.request, json
x = 5
while x == 5:
    with urllib.request.urlopen("https://redisq.zkillboard.com/listen.php") as url:
        data = json.loads(url.read().decode())
        #print(data['package']['killmail']['killmail_id'])
        for i in data:
            #if data['package']['killmail']['victim']['character_id'] == 94418625:
            zkillID = data['package']['killmail']['killmail_id']
            newurl = "zkillboard.com/kill/{0}".format(zkillID)
            print(newurl)
            time.sleep(10)
            #else:
                #break
