import  os
# x = input('Enter your name:')
# x="hair"
github_sha=os.environ["GITHUB_SHA"]
UID=os.environ["ES_UID"]
print("Hello ",os.environ["GITHUB_SHA"])
folder=UID+"_yoBRO"
os.mkdir(folder)

#print("Bro this is the value ",os.environ.get("UID"))