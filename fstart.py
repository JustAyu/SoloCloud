import os
#It just a simple script to save my time on vps HAHA
try:
	os.system("tmux")
	os.system(f"kill -9 {os.getpid()} && rm cache && python3 -m prime")
except:
	os.system(f"kill -9 {os.getpid()} && rm prime.session && python3 -m prime")


# Please do not think that I am using code as bad, If you think like that then fuck off! I never care about public's suggestions!