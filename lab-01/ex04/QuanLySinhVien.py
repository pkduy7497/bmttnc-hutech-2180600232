#tạo class QLSV từ from SV
from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []
    
    def generateID(self):
        maxId = 1
        if(self.soluongSinhVien() > 0):
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if(maxId < sv._id):
                    maxId = sv._id
            maxId = maxId + 1
        return maxId
    
    def soluongSinhVien(self):
        return self.listSinhVien.__len__()
    
    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhập tên SV: ")
        sex = input("Nhập giới tính SV: ")
        major = input("Nhập chuyên ngành của SV: ")
        diemTB = float("Nhập điểm TB của SV: ")
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xeploaiHocLuc(sv)
        self.listSinhVien.append()
    
    def updateSinhVien(self, ID):
        sv:SinhVien = self.findByID(ID)
        if(sv != None):
            svId = self.generateID()
            name = input("Nhập tên SV: ")
            sex = input("Nhập giới tính SV: ")
            major = input("Nhập chuyên ngành của SV: ")
            diemTB = float("Nhập điểm TB của SV: ")
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xeploaiHocLuc(sv)
        else:
            print("SV có ID = {} không tồn tại.".format(ID))
    def sortByID(self):
        self.listSinnVien.sort(key=lambda x: x._id, reverse=False)
    
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)
        
    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False)
        
    def findyID(self, ID):
        searchResult = None
        if (self.soluongSinhvien() > 0):
            for sv in self.listSinhvien:
                if (sv._id == ID):
                    searchResult = sv
        return searchResult
    
    def findByName(self, keyword):
        listSV = []
        if (self.soluongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV

    def deleteById(self, ID):
        isDelete = False
        sv = self.findByID(ID)
        if(sv != None):
            self.listSinhVien.remove(sv)
            isDelete = True
        return isDelete
    
    def xeploaiHocLuc(self, sv:SinhVien):
        if (sv._diemTB >=8):
            sv._hocLuc = "Giỏi"
        elif (sv._diemTB >=6.5):
            sv._hocLuc = "Khá"
        elif(sv._diemTB >=5):
            sv._hocLuc = "Trung Bình"
        else:
            sv._hocLuc = "Yếu"
    
    def showSinhVien(self, listSV):
        print("{:<8} {:<8} {:<8} {:<8} {:<8}".format("ID", "Name", "Major", "Diem TB", "Hoc Luc"))
        if(listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<8} {:<8} {:<8} {:<8}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
                print("\n")
                
    def getListSinhVien(self):
        return self.listSinhVien