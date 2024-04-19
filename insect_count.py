import os

filepath = r'map_out/image_locations'
insect_count = 0
file_count = 0
one_insect_num = 0
savepath = r'map_out/count_file'

for root, dirs, files in os.walk(filepath):
    for filename in files:
        with open(filepath + '/' + filename) as file:
            content = file.read()   #read all text by string
            one_insect_num = content.count("insect")    #find the words which you need and count its numher in this string
            print('当前文件' + filename + '的昆虫数量是：', one_insect_num)
            con = str(one_insect_num)
            with open(os.path.join(savepath, filename), 'a') as new_f:
                new_f.write(con)
            insect_count = insect_count + one_insect_num
            file_count = file_count + 1


print('总的文件数量是：', file_count)
print('总的昆虫数量是：', insect_count)

