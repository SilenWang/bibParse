'''
需要用Post请求, 因为doi这类的内容一定有特殊字符
'''

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

try:
    from .utils import search_identifier
except ImportError:
    from utils import search_identifier


class Query(BaseModel):
    '''
    请求体, 只包含文献的ID
    '''
    Identifier: str


class Paper(BaseModel):
    '''
    响应体数据部分, 包含解析完成的文献信息
    '''
    doi: str
    title: str
    journal: str
    journalAbbr: str
    abstract: str
    pubDate: str
    authors: List[str]


class Data(BaseModel):
    '''
    响应体, 按照原来的格式, 包括code, msg, data三部分内容
    '''
    code: int
    msg: str
    data: Paper


router = APIRouter()

@router.post(
    '/parse', 
    summary = '根据doi或者pmid解析文献信息',
    response_model = Data,
    status_code = 201
)
async def bibParse(query: Query):
    statusCode, statusText, res = search_identifier(query.Identifier)
    if statusCode == 200:
        return {'code': 0, 'msg': 'success', 'data': res}
    elif statusCode == 501 and statusText == 'No items returned from any translator':
        return {
            'code': 1,
            'msg': f"Paper Not Found using id {query.Identifier}, this may due to network error, you can try agin",
            'data': {}
        }
    elif statusCode == 501:
        return {
            'code': 1,
            'msg': f"Paper Not Found using id {query.Identifier}, please use another one",
            'data': {}
        }
    else:
        raise HTTPException(status_code=501, detail="Unknown Error From Server Side")

