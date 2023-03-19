# for i in range (100,141):
#     indexfile = str(i)
#     namefile ="src\\test\solutions\\"+ indexfile + ".txt"
#     f=open(namefile,"r+")
#     linef = f.readlines()
#     j=0
#     for lineff in linef:
#         if linef[j].find("\\")>0:
#             linef[j]=linef[j].replace('\\','\\\\')
#             f.seek(0)
#             f.truncate()
#             f.writelines(linef)
#             print(namefile)
#         j=j+1
#     f.close()
#     f=open(namefile,"r")
#     content = f.read()
#     print(content)
#     test = open("src\\test\solutions\\test.txt", "r+")
#     lines=test.readlines()
#     index = 0
#     for line in lines:
#         if line.find("successful")>0:
#             lines[index] = "        expect =" + "\"\"\"" + content + "\"\"\" \n"
#             print(lines[index])
#             test.seek(0)
#             test.truncate()
#             test.writelines(lines)
#             break
#         index = index+1
#     f.close()
#     f=open(namefile,"r+")
#     j=0
#     for lineff in linef:
#         if linef[j].find("\\\\")>0:
#             linef[j]=linef[j].replace('\\\\','\\')
#             f.seek(0)
#             f.truncate()
#             f.writelines(linef)
#             print(namefile)
#         j=j+1


test = open("src\\test\solutions\\test.txt", "a")
for i in range(141,200):
    defff = "    def test_case_"+str(i)+"(self):"
    test.write(defff+ "\n")
    test.write("        #Day la input va expect\n")
    expect = "        self.assertTrue(TestAST.test(input, expect, "+ str(i)+"))"
    test.write(expect + "\n")
