read_f = open("H:\\课程学习\\Information Security & Privacy\\homework\\code\\1.txt","rU");
write_f = open("H:\\课程学习\\Information Security & Privacy\\homework\\code\\2.txt","a+");
content = read_f.read()
write_f.write(content.replace('\n',','))