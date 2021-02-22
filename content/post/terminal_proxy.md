+++
date = 2019-08-16T08:16:57
title = "给终端设置代理"
[taxonomies]
tag = ["shell"]
+++

今天`brew`跟新包的时候, 速度是真的慢. 需要给终端设置代理, 一两条命令能搞定.
切换代理算是日常操作, 于是写个小函数方便使用.
```bash
proxy_st=off
toggle_proxy() {
    if [ "$proxy_st" = on ]; then
        unset ALL_PROXY
        proxy_st=off
        echo proxy is now "$proxy_st"
    else
        export ALL_PROXY="socks5://localhost:1080"
        proxy_st=on
        echo proxy is now "$proxy_st"
    fi
}
```
之后切换代理就会比较方便了. 如果想在开启新终端时就启用代理, 在`rc`文件中调用一次该函数即可.

{% note() %}
一个小问题, 这个proxy_st变量会存在于全局范围. bash中该怎么声明函数范围的static变量呢?
{% end %}
