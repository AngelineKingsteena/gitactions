import  os
# x = input('Enter your name:')
# x="hair"
github_sha=os.environ["GITHUB_SHA"]
print("Hello ",os.environ["GITHUB_SHA"])
folder=github_sha+"_yoBRO"
os.mkdir(folder)

#print("Bro this is the value ",os.environ.get("UID"))