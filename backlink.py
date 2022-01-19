import json,requests,re,sys
try:
  if (sys.version_info.major == 3):
    site = input(" => Backlink Url Site\t: ")
  else:
    site = raw_input(" => Backlink Url Site\t: ")
  with open("urlbacklinks.json", "r") as file:
    data = json.loads(file.read())
    for backlink in data:
      url = backlink['url'].replace("h4link.duckdns.org", site)
      try:
        r = requests.get(url).status_code
      except KeyboardInterrupt:
        sys.exit()
      except:
        r = "time out"
      print(site + " => backlinked  ==> "+re.search('http:\/\/.*?\/', url).group(0).replace("/", "").replace("http:","") + " status: "+str(r))
except:
  print("\n\n => exit\n")
