import subprocess

# Global Variable
result = subprocess.run(
    ["ping", "google.com"],
    stdout=subprocess.PIPE,
    stdin=subprocess.PIPE,
    text=True,
    check=True
)

try:
    print(result)

except subprocess.CalledProcessError as e:
    print(result.stderr)
