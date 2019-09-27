from IPython.display import HTML
import os
CDSW_ENGINE_ID = os.environ["CDSW_ENGINE_ID"]
CDSW_DOMAIN = os.environ["CDSW_DOMAIN"]
host = CDSW_ENGINE_ID+"."+CDSW_DOMAIN
print(host)



from IPython.display import HTML


bla = '<iframe width="1000" height="1000" src="http://'+host+'/#graphs"></iframe>'
bla = '\''+bla + '\''

print(bla)

HTML(eval(bla))
