import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd
import cdsw


df_model = pd.read_csv("/home/cdsw/demo/hdfs/training.log", delimiter=",")
df_classifier = pd.read_csv("/home/cdsw/demo/hdfs/classifier_training.log", delimiter=",")


#print(plt.style.available)
#style.use('seaborn-talk') bmh, ggplot, seaborn-colorblind

style.use('bmh')


def train_model():
  
  model_name = "Inception3"
  
  # import model & train, with logs to hdfs folder
  # models in /demo/models
  # not run for demo since training will require 24 hours on CPU nodes


def plot_model_acc():

  fig, ax = plt.subplots(nrows=1, ncols=1)
 
  ax.set_facecolor('white') 
  ax.set_xlabel('Epoch')
  ax.set_ylabel('Accuracy')
  ax.set_title('Complete Model Accuracy')

  fig.set_facecolor('white') 
  
  plt.plot( 'epoch', 'acc', label="Accuracy", data=df_model, markersize=12, color='skyblue', linewidth=1)
  plt.plot( 'epoch', 'val_acc', label="Validation Accuracy", data=df_model, markersize=12, color='blue', linewidth=1)
    
  legend = plt.legend(loc="lower right", facecolor='white', framealpha=1)

  plt.show()

plot_model_acc()



def plot_model_loss():

  fig, ax = plt.subplots(nrows=1, ncols=1)
  
  ax.set_facecolor('white') 
  ax.set_xlabel('Epoch')
  ax.set_ylabel('Loss')
  ax.set_title('Complete Model Loss')
  fig.set_facecolor('white') 
  
  plt.plot( 'epoch', 'loss', label="Loss", data=df_model, markersize=12, color='skyblue', linewidth=1)
  plt.plot( 'epoch', 'val_loss', label="Validation Loss", data=df_model, markersize=12, color='blue', linewidth=1)
  
  legend = plt.legend(loc="lower right", facecolor='white', framealpha=1)
  
  plt.show()

  
  
plot_model_loss()
  
def plot_classifier_acc():

  fig, ax = plt.subplots(nrows=1, ncols=1)

  ax.set_facecolor('white') 
  ax.set_xlabel('Epoch')
  ax.set_ylabel('Accuracy')
  ax.set_title('Classifier Accuracy')
  fig.set_facecolor('white') 
  
  plt.plot( 'epoch', 'acc', label="Accuracy", data=df_model, markersize=12, color='skyblue', linewidth=1)
  plt.plot( 'epoch', 'val_acc', label="Validation Accuracy", data=df_model, markersize=12, color='blue', linewidth=1)
    
  legend = plt.legend(loc="lower right", facecolor='white', framealpha=1)
  
  plt.show()

  
plot_classifier_acc()
  
  

  

cdsw.track_metric("Accuracy", 0.9)   
cdsw.track_metric("AUC", 0.95)  