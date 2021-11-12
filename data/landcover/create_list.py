from glob import glob
train_images = glob('images/train/*.jpg')
train_labels = glob('annotations/train/*.png')
f = open("train.lst", 'w')
for i in range(len(train_labels)):
    f.write(str(train_images[i]).replace("\\","/")+'\t'+str(train_labels[i]).replace("\\","/")+'\n')
f.flush()
print('train.lst finished!')

test_images = glob('images/test/*.jpg')
test_labels = glob('annotations/test/*.png')
f = open("test.lst", 'w')
for i in range(len(test_labels)):
    f.write(str(test_images[i]).replace("\\","/")+'\t'+str(test_labels[i]).replace("\\","/")+'\n')
f.flush()
print('test.lst finished!')

val_images = glob('images/val/*.jpg')
val_labels = glob('annotations/val/*.png')
f = open("val.lst", 'w')
for i in range(len(val_labels)):
    f.write(str(val_images[i]).replace("\\","/")+'\t'+str(val_labels[i]).replace("\\","/")+'\n')
f.flush()
print('val.lst finished!')


f = open("trainval.lst", 'w')
for i in range(len(train_labels)):
    f.write(str(train_images[i]).replace("\\","/")+'\t'+str(train_labels[i]).replace("\\","/")+'\n')
for i in range(len(val_labels)):
    f.write(str(val_images[i]).replace("\\","/")+'\t'+str(val_labels[i]).replace("\\","/")+'\n')
f.flush()
print('trainval.lst finished!')