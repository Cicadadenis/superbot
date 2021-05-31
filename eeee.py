import requests
from my_fake_useragent import UserAgent
ua = UserAgent(os_family = 'ios')
res = ua.random()
print('🔴', res, '🔴')