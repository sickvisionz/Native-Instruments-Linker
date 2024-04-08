# Native-Instruments-Linker
A Windows and Python based tool for linking a folder full of Native Instruments libraries at once rather than going into Native Access and linking each and every one of them manually!

I created this tool when my operating system storage drivek died.  Once I installed a new one and put the OS on it, I went to add all of my Native Instruments stuff via Native Access.  My instrument libraries (780+ GB) were on a separate drive so I assumed it would "point it to the root folder and it does the rest.  WRONG!  They wanted me to link each folder 1 by 1.  Things like KOMPLETE come with 200+ instruments meaning 200+ folders to link. I searched on the forums for a better way and came across a thread (https://community.native-instruments.com/discussion/8443/how-about-a-locate-all-function-in-native-access/p1) where someone from NI said a "Locate All" was in the backlog to be implemented.  That was December 2022.  I'm uploading this in April 2024.

This tool isn't perfect but it will speed up your process a lot. **NOTE: This tool directly edits your registry!**  Also, this only locates things that actually have the "Locate" option.

# Instructions
* Step 1: Install Native Access (NA)
* Step 2: Open NA and install your applications
![Install Applications](https://github.com/sickvisionz/Native-Instruments-Linker/assets/38568987/7be996e4-27c5-4b14-8575-d112c7a905a7)
* Step 3: Locate your NativeAccess.xml file.  Mine was in C:\Program Files\Common Files\Native Instruments\Service Center
* Step 4: Download and install Python (https://www.python.org/downloads/)
* Step 5: Download the ni-linker.py file from this git
* Step 6: Run command prompt. Click start, type "command" and it will pop up.
* * I ran mine as an administrator because I thought I might have to in order to make the tool edit the registry
* Step 7: While in the command prompt, navigate to the folder that the ni-linker.py file is in.
* * If you saved it in C:\LinkerTool\ni-linker.py then you'd type in "cd c:\LinkerTool"
* Step 8: Run the script in command prompt.  Type "py ni-linker.py"
* Step 9: The script will ask you two questions.  Answer them.
![image](https://github.com/sickvisionz/Native-Instruments-Linker/assets/38568987/82f742be-f8be-4fde-b6f8-2cc58919c8c8)
* Step 10: After you do that, it'll scroll a bunch of text as it updates your registry.  **It located and linked everything that it could!**
* Step 11: Open NA (or refresh it if you never closed it).  You should now see a bunch of files in your "Updates" area
![Update All](https://github.com/sickvisionz/Native-Instruments-Linker/assets/38568987/8a20ea29-e9f9-4ffd-8df8-c27a437543a1)
* Step 12: Click "Update All"

You'll still have to update some things (or maybe not depending on when you last did an update) but the file sizes are much smaller.  Example: the full Abbey Road drummer packs are well over 7 GB each.  You only need to download 80 to 150 MB to have them up and running.  This is in addition to you having the option to one-click "Update All".
