# warp-action-infinite
配置 GitHub Actions 来刷无限流量

## 刷刷刷方法1

手动下载本地**刷刷刷软件**(`warp-plus-cloudflare \[version3 by aliilapro].exe`)

![截图](https://github.com/warp-plus-cloudflare/gui/blob/main/ScreenShot/Capture.jpg)

使用方法: 
1. 点击**Server1**或者**Server2**配置ProxyList
2. 在**Enter Device ID**下方的输入框中输入**设备ID**

ps. 如何获取**设备ID**，桌面端: 右下角**设置**-->**偏好设置**-->**常规**下面的**设备ID**

下载地址: [warp plus cloudflare](https://github.com/warp-plus-cloudflare) 下的 [gui](https://github.com/warp-plus-cloudflare/gui) 库的最新程序

## 刷刷刷方法2

使用[在线刷网址](https://replit.com/@wdm1732418365/warp)

![image](https://github.com/ACG-Q/warp-action-infinite/assets/47310744/17037a89-fd79-4917-8aea-f9caaedd6503)

使用方法: 
1. 点击右边绿色的**Run**
2. 输入提示中输入**设备ID**


## 刷刷刷方法3

fork 一份仓库

然后在Actions secrets and variables(**Setting**-->**Secrets and variables**-->**Actions**)中创建`DEVICEID`并填写**设备ID**

![image](https://github.com/ACG-Q/warp-action-infinite/assets/47310744/166117b8-ca72-4d48-bb3c-dbc191e13562)

手动触发: 点击**Run workflow**(ps.运行太久就会被强制关闭)

![image](https://github.com/ACG-Q/warp-action-infinite/assets/47310744/d76142d8-1848-4d6f-9901-ac24683a4726)

自动触发: 每天8点33分，自动运行(可以自己修改)
