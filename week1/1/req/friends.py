import requests
import re
import datetime


def calc_age(uid):
    r = requests.get('https://api.vk.com/method/users.get?v=5.71&access_token=17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711&user_ids=' + uid).json()
    id = r['response'][0]['id']

    r = requests.get('https://api.vk.com/method/friends.get?v=5.71&access_token=17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711&user_id=' + str(id) + '&fields=bdate').json()

    years = []
    for item in r['response']['items']:
        try:
            now = datetime.datetime.now()
            year = re.search(r'\d{4}', item['bdate'])
            years.append(now.year - int(year.group(0)))
        except:
            pass

    pre_result = {i: years.count(i) for i in years}

    result = []
    for i in sorted(pre_result.items(), key=lambda para: (-para[1], para[0])):
        result.append(i)

    return result

def find_all_digits(text):
    exp = r'\d+'  #Тут напишите своё регулярное выражение
    return re.findall(exp, text)

if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)
    print(find_all_digits('a123b45с6d'))
