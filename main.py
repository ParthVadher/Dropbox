# class Car:
#     def __init__(self,brand,model,color):
#         self.brand=brand
#         self.model=model
#         self.color=color
#
#     def theCarIs(self):
#
#         print("Welcome " +self.brand+ " user.")
#
# c1 = Car("BMW","Serie-A","Black")
# c2 = Car("Ferrari","LaFerrar","Red")
# c3 = Car("Tesla","Model-Y","White")
#
# c1.theCarIs()
# print(c1.model)
# print(c1.color)
#
# c2.theCarIs()
# print(c2.model)
# print(c2.color)
#
# c3.theCarIs()
# print(c3.model)
# print(c3.color)

import dropbox


class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):

        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.AbKQY7cwlr949HZB7JxLOMrnYKuY39PSkiEnMjmzkLJ8mukldzSQjT8oLVfn_A-kB4yn6O0erRD07aV-9JeaGvvRPoLFEVvwg3_p2AufnKjhGlCgTVtpR4YV0SKhk6nbU2-ztZAB'
    transferData = TransferData(access_token)

    file_from = "C:\\Users\\Dell\\Desktop\\pythonProject1\\main.py"
    file_to = "\\Project\\main.py"


    transferData.upload_file(file_from, file_to)
    print("The File has been moved :)")

main()