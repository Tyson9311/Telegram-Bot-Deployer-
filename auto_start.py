import os
import subprocess

def auto_start_bots():
    bots = [d for d in os.listdir('/app/hosted_bots') if os.path.isdir(os.path.join('/app/hosted_bots', d))]
    
    for bot in bots:
        subprocess.run(["docker", "start", bot])

if __name__ == "__main__":
    auto_start_bots()
