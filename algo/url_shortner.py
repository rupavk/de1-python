import random
import string
dictinary1,dictionary2
function shorterUrl(url):
       if(dictionary[url]):
            return dictionary[url]
else:
     dictionary1.Add(url,''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8)))
     dictionary2.Add(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8)),url)
      return dictionary[url],


function restoreurl(short)
  if (dictionary2(short)):
    return dictionary[short]
  else 
    return null

    
if __name__ == '__main__':
    pass

