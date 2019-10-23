from IPython.display import HTML
import os
CDSW_ENGINE_ID = os.environ["CDSW_ENGINE_ID"]
CDSW_DOMAIN = os.environ["CDSW_DOMAIN"]
host = CDSW_ENGINE_ID+"."+CDSW_DOMAIN
print(host)



from IPython.display import HTML


bla = '<iframe width="900" height="2800" scrolling="no" frameborder="0" src="http://'+host+'"></iframe>'
bla = '\''+bla + '\''

print(bla)

HTML(eval(bla))
