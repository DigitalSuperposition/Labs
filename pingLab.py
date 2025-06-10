import subprocess

#Global Variable


try: 
    result = subprocess.run(["ping",  "google.com"], capture_output=True, text=True, check=True]) #Make a simpler global variable
    print(result) 

except:
    subprocess.CalledProcessError 	
    print(result.stderr)
  
result = subprocess.run(["ping",  "google.com"], capture_output=True, text=True, check=True)



