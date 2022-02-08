from distutils.command.upload import upload
from os import access
import dropbox 
class TransferData:
    def __init__(self,acess_token):
        self.acess_token = acess_token
    def uploadfile (self,filefrom,fileto):
        dbx = dropbox.Dropbox(self.acess_token)
        f = open(filefrom,"rb")
        dbx.files_upload (f.read(),fileto)
def main():
    acess_token = "sl.BBX0oHu3M6btXJtSoZZNhWK-8I0qvEm9X3JUX8KryGPcxAk6oHkF7DReHgscB0vz6JrbTcvVPDYoRNiv-xDJC22cog4fEHzag5mQbvOwKOZUk9I0fnfFkM_j-TQWzUzcpyS9OXA"
    transferData = TransferData(acess_token)
    filefrom = input("enter file name ")
    fileto = "/cloudStorage/sample.txt"
    transferData.uploadfile(filefrom,fileto)
    print ("File Has Been Moved")
main()