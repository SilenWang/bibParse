目标是使用FAST-API构建一个解析文献详细信息的API

- 输入: doi(带有符号)号码或者pmid(纯数字)
- 输出: 插入文献必须的题录信息
  + [x] 题目
  + [x] 摘要
  + [x] 杂志
  + [x] 作者
  + [x] 刊发年月 

经查询, Zotero团队的开源项目`translation-server`可以直接调用项目内成熟的`translator`, 将各种信息解析出来返回


## Todo

- [x] 使用FAST-API对`translation-server`进行套壳
- [ ] 将准备好的内容形成一个容器
- [ ] 使用Python的某种模块给这个API做一个有Web界面的前端
- [ ] 通过`SciHub`直接获取文献PDF