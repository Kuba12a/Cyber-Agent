# Cyber-Agent

### 1. Run FastApi
To run fastApi you need to have hypercorn server installed
```
pip install "hypercorn[trio]"
```
Run fastApi using hypercorn
```
hypercorn Api/CommandApi:app --bind ip_address:port

```
