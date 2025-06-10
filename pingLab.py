import subprocess

#Global Variable
result = subprocess.run(["ping",  "google.com"], capture_output=True, text=True, check=True]) #Make a simpler global variable
    
try: 
    print(result) 

except:
    subprocess.CalledProcessError 	
    print(result.stderr)
