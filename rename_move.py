import os,shutil
count = 0

txt_file = open("images_val.txt", "r")
lines = txt_file.read().split('\n')

path = '/home/naman/Downloads/Retail Pulse ML Assignment Data/val/'
for i in sorted(os.listdir(path)):
    files = os.listdir(path + str(i))
    files = sorted(files)
    b = []

    for j in range(count, count + len(files)):
        b.append(lines[j])
    count = count + len(files)

    for img, extra in zip(files, b) :
        filename, extension = os.path.splitext(img)
        os.rename(path + str(i) + '/' + img, ''.join([path, str(i) + '/', extra, extension]))


for i in sorted(os.listdir(path)):
    files = os.listdir(path + str(i))
    # print(i)
    files = os.listdir(path + str(i))
    for f in files:
        shutil.move(path + i + '/' + f, path)
