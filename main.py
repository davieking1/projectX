# import sys
# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QMainWindow, QInputDialog, QLineEdit, QMessageBox, QFileDialog
# from PyQt5.uic import loadUi 
from encryption import Encryption
from decryption import Decryption
# import hashlib
# import os

import hashlib
import os
import re
import sys
import ctypes

import pyperclip
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QInputDialog, QLineEdit
from PyQt5.uic import loadUi

import cryptographer
#import encfile

class Main(QMainWindow):
	filename = None
	spanner = None
	receiver = None
	gibberish = None
	plain = None
	initz = None
	def __init__(self):
		#inheriting from the QMain window class
		super(Main, self).__init__()
		#load ui
		loadUi('main.ui', self)

		#encrypt and decrypt buttons methods
		self.encryptButton.clicked.connect(self.encrypt)
		self.decryptButton.clicked.connect(self.decrypt)
		#self.browseFileButton.clicked.connect(self.open_file)
		self.encryptFileButton.clicked.connect(self.enc_file)
		self.decryptFileButton.clicked.connect(self.dec_file)
		self.browseFileButton.clicked.connect(self.attach_file)
	#encryption class
	# def encrypt(self):
	# 	self.plaintext = self.textEdit.toPlainText()   #get user plaintext to QT text edit
	# 	#prompt user password
	# 	self.passwd, ok = QInputDialog.getText(self, "password", "Kindly enter the password:", QLineEdit.Password, "")
	# 	# if len(self.passwd) < 8:
	# 		# QMessageBox.about(self, "the password lenght should be a minimum of 8 characters")
	# 	#print(passwd)
	# 	#calling the method to encrypt from customCipher1 

	# 	finbin = Encryption(self.plaintext, self.passwd)
	# 	self.finbin_text = finbin.getfinbin()
	# 	self.IV = finbin.getIV()
	# 	self.disp = finbin.display()

	# 	if finbin:
	# 		QMessageBox.about(self, "Encryption Status", "Encryption Completed")
	# 		self.textEdit.clear()
			
	# 		QMessageBox.about(self, "Initialization vector: ", self.IV)
	# 		#self.fileTextEdit.append(self.IV)
	# 		#self.textEdit.append(self.disp)


	# 	else:
	# 		QMessageBox.about(self, "Encryption Status", "Encryption Failed")


	# #decryption class
	# def decrypt(self):
	# 	#self.fbin_text = self.textEdit
	# 	# prompt user password
	# 	finbin_text = self.textEdit.toPlainText()   #get user plaintext to QT text edit

	# 	self.passwd, ok = QInputDialog.getText(self, "password", "Kindly enter the password:", QLineEdit.Password, "")
	# 	self.initial_vector, ok = QInputDialog.getText(self, "IV", "Kindly enter the provided initial vector:", QLineEdit.Password, "")
	# 	#Decryption(self.plaintext, self.passwd)

	# 	get_text = Decryption(finbin_text, self.passwd, self.initial_vector)
	# 	msg = get_text.get_text()
	# 	if get_text:
	# 		QMessageBox.about(self, "Decryption Status", "Decryption Completed")
	# 		self.textEdit.clear()
	# 		self.textEdit.append(msg)
	# 	else:
	# 		QMessageBox.about(self, "Decryption Status", "Decryption Failed")


	def encrypt(self):
		self.plaintext = self.textEdit.toPlainText()   #get user plaintext to QT text edit
		#prompt user password
		self.passwd, ok = QInputDialog.getText(self, "password", "Kindly enter the password:", QLineEdit.Password, "")
		# if len(self.passwd) < 8:
			# QMessageBox.about(self, "the password lenght should be a minimum of 8 characters")
		#print(passwd)
		#calling the method to encrypt from customCipher1 

		finbin = Encryption(self.plaintext, self.passwd)
		self.finbin_text = finbin.getfinbin()
		self.IV = finbin.getIV()
		self.disp = finbin.display()

		if finbin:
			QMessageBox.about(self, "Encryption Status", "Encryption Completed")
			self.textEdit.clear()
			self.textEdit.append(self.disp)
			QMessageBox.about(self, "Initialization vector: ", self.IV)
			self.fileTextEdit.append(self.IV)


		else:
			QMessageBox.about(self, "Encryption Status", "Encryption Failed")


	#decryption class
	def decrypt(self):
		#self.fbin_text = self.textEdit
		# prompt user password
		#finbin_text = self.textEdit.toPlainText()   #get user plaintext to QT text edit
		finbin_text = self.finbin_text

		self.passwd, ok = QInputDialog.getText(self, "password", "Kindly enter the password:", QLineEdit.Password, "")
		self.initial_vector, ok = QInputDialog.getText(self, "IV", "Kindly enter the provided initial vector:", QLineEdit.Password, "")
		#Decryption(self.plaintext, self.passwd)

		get_text = Decryption(finbin_text, self.passwd, self.initial_vector)
		msg = get_text.get_text()
		if get_text:
			QMessageBox.about(self, "Decryption Status", "Decryption Completed")
			self.textEdit.clear()
			self.textEdit.append(msg)
		else:
			QMessageBox.about(self, "Decryption Status", "Decryption Failed")

	def open_file(self):
		self.fname = QFileDialog.getOpenFileName(self)
		self.f_path = self.fname[0]
		self.fpath.setText(self.f_path)



	def attach_file(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getOpenFileName(self, 'Select File', os.path.expanduser('~/Documents'))
		if fileName:
			try:
				self.filename = fileName
				self.fpath.setText(fileName)
			except:
				return None

	def write_file(self, data):
	    pdir = os.getcwd()
	    outPut_file = pdir+"/temporary.txt"
	    print(outPut_file)
	    with open(outPut_file, "w") as out_file:
	        # write bytes to file
	        out_file.write(data)
	        out_file.close()
	    return outPut_file

	def read_file(self, outfile):
	    filename = outfile
	    with open(filename, "r") as infile:
	        file = infile.read()
	    return file

	def enc_file(self):
	    if self.filename:
	        self.setEncryptPassword()
	        self.fileEncrypt()
	        QMessageBox.about(self, "Status", "File Encrypted and \nSaved Successfully")
	        # if self.spanner is not None:
	        #     if self.gibberish is not None:
	        #         self.saver()
	        #     else:
	        #         QMessageBox.about(self, "Status", "File Encrypted and \nSaved Successfully")
	        #         self.cancel()
	        # else:
	        #     return None

	    else:
	        QMessageBox.about(self,"Status","No File to Encrypt")
	        self.cancel()

	def fileEncrypt(self):
	    if self.filename is None:
	            return None
	    else:
	        if ".enc" not in self.filename:

	            self.filename = os.path.join(self.filename)

	            self.initz = hashlib.sha256(self.spanner.encode()).digest()
	            # self.initz = self.spanner.encode()
	            print(self.initz)
	            keyfile=self.initz
	            filename=self.filename
	            cryptographer.Crypto.encryption(filename=filename, keyfile=keyfile)
	            self.filename = self.filename + '.enc'
	            self.fpath.setText(self.filename)
	        else:
	            QMessageBox.about(self, "Status", "File already encrypted")



	def dec_file(self):

	    if self.filename is None:
	        return None
	    else:
	        self.filename = os.path.join(self.filename)
	        filename = self.filename
	        text, ok = QInputDialog.getText(self, "Password", "Kindly enter the decryption password:", QLineEdit.Password, "")
	        if text != '':
	            if ok:
	                if ".enc" in self.filename:
	                    self.spanner = text
	                    keyfile = hashlib.sha256(self.spanner.encode()).digest()
	                    # keyfile = self.spanner.encode()
	                    print(filename)
	                    print(keyfile)
	                    # y =  bin(int.from_bytes(keyfile, 'big'))
	                    # print(y)
	                    cryptographer.Crypto.decryption(filename=filename,keyfile=keyfile)
	                    self.spanner = None
	                    QMessageBox.about(self, "Status", "File Decrypted and \nSaved Successfully")
	                else:
	                    QMessageBox.about(self, "Decryption Status", "Already in plain text")

	            else:
	                return None
	        else:
	            if ok:
	                self.dec_file()
	            else:
	                return None



	def cancel(self):
	    self.filename = None

	def setEncryptPassword(self):
	    text, ok = QInputDialog.getText(self, "Password",
	                                        "Kindly enter the encryption password:", QLineEdit.Password, "")
	    if text != '':
	        if ok:
	            flag = 0
	            while True:
	                if (len(text) < 8):
	                    flag = -1
	                    break
	                elif not re.search("[a-z]", text):
	                    flag = -1
	                    break
	                elif not re.search("[A-Z]", text):
	                    flag = -1
	                    break
	                elif not re.search("[0-9]", text):
	                    flag = -1
	                    break
	                elif not re.search("[_@$!#%^&*-=+()}{?']", text):
	                    flag = -1
	                    break
	                elif re.search("\s", text):
	                    flag = -1
	                    break
	                else:
	                    flag = 0
	                    self.spanner = text
	                    self.confirmPassword()

	                    break

	            if flag == -1:
	                QMessageBox.about(self, "Weak password", "Password should contain:\n-Atleast 8 Characters\n-Uppercase\n-Lowercase\n-Numerals &\n-Special Characters")
	                self.setEncryptPassword()
	        else:
	            return None
	    else:
	        if ok:
	            self.setEncryptPassword()
	        else:
	            return None


	def confirmPassword(self):
	    text, ok = QInputDialog.getText(self, "Confirmation",
	                                    "Kindly Re-enter the encryption password:", QLineEdit.Password, "")
	    if text != '':
	        if ok:
	            nut = text
	            if nut == self.spanner:
	                self.spanner = nut

	            else:
	                QMessageBox.about(self, "Miss-Match", "Password do not match \n Please re-enter")
	                self.setEncryptPassword()
	        else:
	            pass

	    else:
	        if ok:
	            QMessageBox.about(self, "Error", "Password not confirmed")
	            self.setEncryptPassword()
	        else:
	            pass







if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	#what i want to show
	window = Main()
	window.show()
	sys.exit(app.exec_())