import re
import time
num_list = {'一' : 1, '二' : 2, '三' : 3, '四' : 4, '五' : 5, '六' : 6, '七' : 7, '八' : 8, '九' : 9,'十':10}
str = "[一二三四五六七八九十]"
s='deng三秒deng'
ans = re.search(str,s).group()
num = num_list.get(ans)
time.sleep(num)
print("jiangzai"+num)