import os

currentDir = os.path.abspath(os.getcwd())
targetFolder = input("targetFolder: ")
targetName = input("targetName: ")
framerate = input("frame rate: ")

print(currentDir)
def save():
    os.system('ffmpeg -start_number 0 -r {} -i {}\{}\%d.png -vcodec mpeg4 -y {}\{}.mp4'.format(framerate, currentDir, targetFolder,  targetFolder, targetName))
save()
