+++
date = 2019-09-23T20:07:03+08:00
title = "使用手机更新GitHub Pages"
[taxonomies]
tag = ["blog"]
+++
这篇文章将介绍如何使用手机更新GitHub Pages文章. 本文也是自己第一次使用手机完成并发布.

## 准备工作
1. markdown(md)编辑器. 我使用的是iOS平台的Bear Notes未付费版本, 插入md标记很方便, 比系统自带的Notes更适合md的书写. iOS平台上的Drafts app付费版本功能更加强大, 其内建的js脚本功能会使体验更加一条龙. 安卓应该有更多的选择.
2. iOS自动化工具Shortcuts. 用于上传md文章的内容.
3. GitHub Actions. GitHub现在支持CI/CD了. 在md文件上传到远程仓库后, 拉取, 构建, 并提交. 本文不做详细讨论. 首次接触的可以看下我博客的workflow, 用的Zola构建. 官方的文档和GitHub Marketplace有更详细的说明和现成的用例.
4. Personal Access Token. 在GitHub settings > developer settings > personal access tokens中生成一个即可

## 手机端配置
GitHub Pages静态博客的CI/CD之前就配置好了, 有了这些铺垫, 本文介绍的手机端配置主要就是Shortcuts的内容.  
根据官方的REST [API](https://developer.github.com/v3/repos/contents/#create-or-update-a-file), 创建文件请求为`PUT /repos/:owner/:repo/contents/:path`.  
请求头必填字段有`Authorization, Accept, User-Agent`.  
请求体为Json格式, 必填的有commit `message`, `committer`, 和base64编码的content(即markdown文本).  
HEADERS:
```yaml
Authorization: token $personal_access_token
Accept: application/vnd.github.v3+json
User-Agent: $user_name
```
Request Body:
```json
{
  "message": "new post",
  "committer": {
    "name": "iphone shortcut",
    "email": "shortcut@bot.com"
  },
  "conetent": "$base64(new_post.md)"
}
```
响应201即发送成功(构建失败默认有邮件通知).

---
Zola的每篇博客需要固定格式的front matter, 而Bear没有模板的支持, 所以我把front matter的生成放在了Shortcuts里面, 这里就不再赘述了.
