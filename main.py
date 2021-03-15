import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        with open(file_from, "rb") as f:
            dbx.files_upload(f.read(), file_to)

def main():
    auth_token = 'sl.AqlVO4Zqvar3M8SJSozVC-nX0p4R4yHIiPjLUsAZ0dFwgptuFEiPn2YhbGhoima5gnwGF_jzPBLReZ8SiZ-EbR55diEoEOgay2Q47yPBV289KinakHyHqNpuG50NEPaV8o6M5gw'
    transfer_data = TransferData(auth_token)
    file_from = r"C:\test\abc.txt"
    file_to = "/test"
    transfer_data.upload_file(file_from, file_to)
    print("Completed!")

if __name__ == "__main__":
    main()
