os.chdir('/home/cdsw/demo/models')



!pip2 install tensorflow
!pip2 install keras
!pip2 install sklearn
!pip install scipy --upgrade

#os.system('nohup /home/cdsw/.local/bin/tensorboard --logdir /home/cdsw/demo/tensorboard/tf_files/training_summaries --port  8090 --host localhost &')


!/home/cdsw/.local/bin/tensorboard --logdir /home/cdsw/demo/tensorboard/tf_files/training_summaries --port  8090 --host localhost 
