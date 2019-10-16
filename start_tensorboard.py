import subprocess
import wait

print("Starting Tensorboard...")

def tensorboard(fname):
    url = ("http://" + os.environ["CDSW_ENGINE_ID"] +
           ".consoles." + os.environ["CDSW_DOMAIN"])
    tb = "/home/cdsw/.local/bin/tensorboard"
    FNULL = open(os.devnull, 'w')
    proc = subprocess.Popen([tb, "--logdir=%s" % fname,
                             "--port=%s" % os.environ["CDSW_READONLY_PORT"]],
                            stdout=FNULL, stderr=FNULL)
    wait.tcp.open(int(os.environ["CDSW_READONLY_PORT"]))
    return url, proc.pid
  
  
tensorboard("/home/cdsw/demo/tensorboard/tf_files/training_summaries")

