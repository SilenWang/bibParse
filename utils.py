'''
调用部署好的Zotero API, 获取文献信息
'''

import requests

def search_identifier(identifier):
    '''
    将得到的编号提交给
    '''

    headers = {
        'Content-Type': 'text/plain'
    }

    urlBase = 'http://127.0.0.1:1969/search'

    response = requests.post(urlBase, data=identifier, headers=headers)

    resDict = response.json()[0]

    return {
        'title': resDict['title'],
        'journal': resDict['publicationTitle'],
        'journalAbbr': resDict['journalAbbreviation'],
        'abstract': 'No abstract.' if 'abstractNote' not in resDict else resDict['abstractNote'],
        'pubDate': '-'.join(resDict['date'].split('-')[:2]),
        'authors': [
            f"{item['firstName']} {item['lastName']}" for item in resDict['creators'] if item['creatorType'] == 'author'
        ] # 可能是zotoero通用才有类型的区分?
    }


if __name__ == '__main__':
    identifier = '10.2307/4486062'
    res = search_identifier(identifier)
    # print(res.status_code)
    print(res)