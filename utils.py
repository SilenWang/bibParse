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
    
    if response.status_code == 200:
        resDict = response.json()[0]
        return response.status_code, response.text, {
            'doi': resDict['DOI'],
            'title': resDict['title'],
            'journal': resDict['publicationTitle'],
            'journalAbbr': resDict['journalAbbreviation'],
            'abstract': 'No abstract.' if 'abstractNote' not in resDict else resDict['abstractNote'],
            'pubDate': '-'.join(resDict['date'].split('-')[:2]),
            'authors': [
                f"{item['firstName']} {item['lastName']}" for item in resDict['creators'] if item['creatorType'] == 'author'
            ] # 可能是zotoero通用才有类型的区分?
        }
    
    else:
        return response.status_code, response.text, {}


if __name__ == '__main__':
    identifier = '28623886'
    code, txt, res = search_identifier(identifier)
    print(code)
    print(txt)