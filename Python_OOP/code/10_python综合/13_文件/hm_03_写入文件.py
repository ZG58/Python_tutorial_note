# 1. 打开
file = open("README", "a")

# 2. 写入文件
file.write("\n123 hello")

# 3. 关闭
file.close()

file = open("README")

text = file.read()
print(text)

file.close()