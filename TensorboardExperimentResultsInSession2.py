import os
CDSW_ENGINE_ID = os.environ["CDSW_ENGINE_ID"]
CDSW_DOMAIN = os.environ["CDSW_DOMAIN"]
host = CDSW_ENGINE_ID+"."+CDSW_DOMAIN
print(host)

!.local/bin/tensorboard --logdir /home/cdsw/demo/tensorboard/tf_files/training_summaries --port  8081 --host localhost 



from IPython.display import HTML
HTML('<iframe width="1000" height="1000" src="http://mzkkwts5nwvjlluf.skiaie-4.vpc.cloudera.com/#graphs"></iframe>')

      '<iframe width="1000" height="1000" src="mzkkwts5nwvjlluf.skiaie-4.vpc.cloudera.com/#graphs"></iframe>'

bla = '<iframe width="1000" height="1000" src="http://'+host+'/#graphs"></iframe>'
bla = '\''+bla + '\''

print(bla)

HTML(eval(bla))

HTML('<iframe width="1000" height="1000" src="'+host+'/#graphs"></iframe>')
     
print ('<iframe width="1000" height="1000" src="'+host+'/#graphs"></iframe>')