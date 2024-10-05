

import os
import shutil


 # Define the directory to organize
directory_to_organize=r'C:\Users\aslah\OneDrive\Desktop\New folder'


# Available Extension dict

extenions_dict={
"Documents":[".txt",".odp",".docx",".pdf",'.html'],
"Images":[".png",".jpeg",".jpg",".svg"],
"Audio":[".mp3",".wav"],
"Video":[".avi",".mov",".mkv",".mp4"],
"Archives":[".zip",".rar",".7z",".tar"]

}


# Create folders

for folder in extenions_dict.keys():
	folder_path=os.path.join(directory_to_organize,folder)
	if not os.path.exists(folder_path):
		os.makedirs(folder_path)
		print(f"directory {folder_path} Created")
		


#function to organize files

def organize_files():
	print(f"Starting to organize...\n")
	
	for item in os.listdir(directory_to_organize):
		item_path=os.path.join(directory_to_organize,item)
		
		
		if os.path.isfile(item_path):
			file_ext=os.path.splitext(item)[1].lower()
			
			for folder_name , extension in extenions_dict.items():
				if file_ext in extension:
					dest_path=os.path.join(directory_to_organize,folder_name,item)
					shutil.move(item_path,dest_path)
					print(f"Moved :{item} -> {folder_name}")
					break
		else:
			print(f"\nSkipping directory {item}\n")
			
			
	print("\n \norganized file successfully")			
			
			

if __name__=="__main__":
	organize_files()
