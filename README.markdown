# Tweet Bot


*requires tensorflow 0.12.0*

![](https://img.shields.io/badge/python-3-brightgreen.svg) ![](https://img.shields.io/badge/tensorflow-0.12.0-yellowgreen.svg) ![](https://img.shields.io/badge/tweepy-3.5.0-yellow.svg)


## Setup


**pull pretrained model**

```bash
# pull metadata
wget -c 'https://www.dropbox.com/s/d35skwq8hk2ljbr/metadata.pkl?dl=0' -O metadata.pkl
# pull pretrained model
cd ckpt
./pull
cd ..
```

**setup twitter bot**

1. Create an account
2. Connect mobile phone with your account
3. Create an [app](https://apps.twitter.com/)
4. Open up the app settings; go to "Keys and Access Tokens"
5. Grab *consumer key/API key*, *consumer secret/API secret* ; save locally
6. Create access token; save *access token*, *access token secret* locally
7. Note down *Owner ID* and your handle


```bash
# need 'tweepy' module
sudo -H pip3 install --upgrade tweepy
# clone repository
git clone https://github.com/suriyadeepan/tweet_bot
cd tweet_bot
# download template config file
wget -c 'https://raw.githubusercontent.com/twitterdev/sample-python-autoreply/master/.twitter.sample' -O .twitter.sample
# **fill in .twitter.sample with keys and tokens**
#
# setup complete
```

## Execute


**chatbot**

```python
import chatbot
# >> Initializing data
# >> Initializing model
# <log> Building Graph </log>
# >> Loading pretrained model
# >> Initialization complete; call respond(msg)
chatbot.respond('Hey! Good morning.. Have a nice day.')
# 'have a wonderful weekend'
```

**autoreply**

```bash
# checklist
# - [ ] download pretrained model and metadata
# - [ ] fill in access keys and tokens in .twitter.sample
python3 autoreply.py
```
