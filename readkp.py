import glob

def keypointReader(pathname):

    with open(pathname + '/kp/keypoints.txt') as f:
        lines = f.read().splitlines()
#print(lines[1])
    line = lines[2].split(' ')[0].split('.')

    newf=[]
    key=0
    dict = {}
    pl = len(pathname)
    for i in glob.glob(pathname + '/testA/*.jpg'):
        key = i
        for l in lines:
            if i.split(' ')[0].split('.')[0][pl+7:] == l.split(' ')[0].split('.')[0]:
                line = list(filter(('').__ne__, l.split(' ')))
                dict[key]={'lex':int(line[1]), 'ley':(int(line[2])-78), 'rex':int(line[3]), 'rey':(int(line[4])-78), 'nx':int(line[5]) , 'ny': (int(line[6])-78), 'lmx':int(line[7]), 'lmy':(int(line[8])-78), 'rmx': int(line[9]), 'rmy':(int(line[10])-78)} #newf.append(l)
    for i in glob.glob(pathname + '/trainA/*.jpg'):
        key = i
        for l in lines:
            if i.split(' ')[0].split('.')[0][pl+8:] == l.split(' ')[0].split('.')[0]:
                line = list(filter(('').__ne__, l.split(' ')))
                dict[key]={'lex':int(line[1]), 'ley':(int(line[2])-78), 'rex':int(line[3]), 'rey':(int(line[4])-78), 'nx':int(line[5]) , 'ny': (int(line[6])-78), 'lmx':int(line[7]), 'lmy':(int(line[8])-78), 'rmx': int(line[9]), 'rmy':(int(line[10])-78)} #newf.append(l)

    return dict
