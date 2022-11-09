# Virtual File System!

import os

device=input("Enter device name: ")
directory=input("Enter directory name: ")
size=input("Enter size of file system(in mb): ")			#Size of file system required.
size=int(size)*2048
print ("Creating file")
os.system("dd if=/dev/zero of="+device+" count="+str(size))
print ("Creating ext3 file system")
os.system("mkfs -t ext3 -q "+device)					#To make ext3 file system.
print ("Creating directory")
os.system("mkdir "+directory)
print ("Mounting file system")
os.system("sudo mount -o loop=/dev/loop0 "+device+" "+directory)	#Mounting loop device
os.chdir(directory)
var = 0
while var!=11:
	print("\n1. Create directory")
	print("2. Print current working directory")
	print("3. Change directory")
	print("4. Remove empty directory")
	print("5. Remove directory recursively")
	print("6. Print contents of directory")
	print("7. Create file")
	print("8. Rename file")
	print("9. Display status of file or file system")
	print("10. Delete file")
	
	var =	input("Enter option: ")
	
	if(var =='1'):
		s=input("Enter directory name: ")
		if not os.path.exists(s):
			os.mkdir(s)
		else:
			print("Directory "+s+" already exists")

	elif(var =='2'):
		print("Current working directory: "+os.getcwd())

	elif(var =='3'):
		s=input("Enter path: ")
		if os.path.exists(s):
			os.chdir(s)
		else:
			print("Path invalid")


	elif( var =='4'):
		s=input("Enter path: ")
		if os.path.exists(s):
			os.rmdir(s)
		else:
			print("Path invalid")

	elif(var =='5'):
		s=input("Enter path: ")
		if os.path.exists(s):
			os.system("rm -rf "+s)
		else:
			print("Path invalid")

	elif(var =='6'):
		s=os.listdir(os.getcwd())
		for filename in s:
			print(filename)

	elif( var =='7'):
		s=input("Enter file name: ")
		os.system("touch "+s)
		

	elif(var =='8'):
		src=input("Enter source name: ")
		dst=input("Enter new name: ")
		if os.path.isfile(src):
			os.rename(src,dst)
		else:
			print("File not found")

	

	elif( var=='9'):
		s=input("Enter path: ")
		if os.path.isfile(s) or os.path.exists(s):
			info=os.lstat(s)					#Using inode information 
			print("Protection bits: "+str(info.st_mode))
			print("Inode number: "+str(info.st_ino))
			print("Device: "+str(info.st_dev))
			print("Number of hard links: "+str(info.st_nlink))
			print("User ID of owner: "+str(info.st_uid))
			print("Group ID of owner: "+str(info.st_gid))
			print("Size: "+str(info.st_size))
			print("Time of most recent access: "+str(info.st_atime))
			print("Time of most recent content modification: "+str(info.st_mtime))
			print("Time of most recent metadata change: "+str(info.st_ctime))
		else:
			print("Path invalid")

	elif(var =='10'):
		s=input("Enter file name: ")
		if os.path.isfile(s):
			os.remove(s)
		else:
			print("File not found")

	
	else:
		print("Wrong option!")

