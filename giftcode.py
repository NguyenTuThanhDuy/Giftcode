import asyncio
import aiohttp
import time
def read_data_file(filename):
    f = open(filename,"r")
    lines = f.readlines()
    params_list = []
    for i in range(1,len(lines)):
        card_code = lines[0].strip()
        card_server = lines[i][0:4].strip()
        card_role = lines[i].strip()
        card_user = '{}{}'.format(card_role, card_role)
        PARAMS = {
            'Host': 'vn-activity.zlongame.com',
            'pd_acti_cb':'jsonpcard_9889',
            'appkey':'1557392843135',
            'card_user':card_user,
            'card_channel':'2010011001',
            'card_server':card_server,
            'card_role':card_role,
            'card_code':card_code,
            'type':'2',
            '_':'1641819550010'
        }
        params_list.append(PARAMS)
    yield from params_list

def get_tasks(session,headers,URL):
    tasks = []
    for param in read_data_file("giftcode.txt"):
        tasks.append(asyncio.create_task(session.get(url = URL, params = param, headers = headers)))
    return tasks

async def send_request():
    #params_list = read_data_file("giftcode.txt")
    success_count = 0
    URL = "https://vn-activity.zlongame.com/activity/cmn/card/csmweb.do?"
    HEADERS = {'Accept':'*/*',
            'Host':'vn-activity.zlongame.com',
            'User-Agent':'PostmanRuntime/7.29.0',
            'Accept-Encoding':'gzip, deflate, br',
            'Connection':'keep-alive',
            'Referer':'https://laplacem.vtcgame.vn/',
            'Sec-Fetch-Dest':'script',
            'Sec-Fetch-Mode':'no-cors',
            'Sec-Fetch-Site':'cross-site'}
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session,HEADERS,URL)
        total_id = len(tasks)
        responses = await asyncio.gather(*tasks)
        for response in responses:
            print(response.status)
            if response.status == 200:
                success_count += 1
    print("DONE: -- {}/{}".format(success_count,total_id))
    
if __name__ == "__main__":
    start = time.time()
    asyncio.run(send_request())
    end = time.time()
    print("{} seconds".format(end-start))
