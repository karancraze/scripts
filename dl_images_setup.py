import os, shutil, pandas as pd

def setup_img(ogdata_dir, base_dir, tr, te, va, df=None):

    if os.path.isdir(base_dir):
        print ('looks like base dir already exists. Do you want to delete it and create new base dir to shuffle data?')
    if input('press Y to continue and N to stop: ')=='y':
        print('Deleting base dir...')
        shutil.rmtree(base_dir)
    else:
        print('Please input another dir to use as base dir')
        return
        
    os.mkdir(base_dir)
    
    train_dir = os.path.join(base_dir, 'train')
    validation_dir = os.path.join(base_dir, 'validation')
    test_dir = os.path.join(base_dir, 'test')

    if df!=None:
        dataset = pd.DataFrame(columns = ['folder','category','file'])    

    os.mkdir(validation_dir)
    os.mkdir(train_dir)
    os.mkdir(test_dir)

    categories = os.listdir(ogdata_dir)

    for x in range(0,len(categories)):
        train = os.path.join(train_dir,'{}'.format(categories[x]))
        os.mkdir(train)
        validation = os.path.join(validation_dir,'{}'.format(categories[x]))
        os.mkdir(validation)
        test = os.path.join(test_dir,'{}'.format(categories[x]))
        os.mkdir(test)

        files = os.listdir(ogdata_dir + '/{}'.format(categories[x]))

        train_num = int(len(files)*tr)
        val_num = train_num + int(len(files)*te)
        test_num = val_num + int(len(files)*va)

        print ('split for Train: {} Test: {} Val {}'.format(tr, te, va))
        print ('Number of images in Training: {} Validation: {} Testing: {}'.format(int(len(files)*tr), int(len(files)*te), int(len(files)*va)))
        print ('Total of {} images in class {}'.format(train_num + val_num + test_num, categories[x]))

        files[train_num]
        
        for f in range(0,train_num):
            src = os.path.join(ogdata_dir + '/{}'.format(categories[x]), files[f])
            dst = os.path.join(train_dir + '/{}'.format(categories[x]), files[f])
            #print(src)
            #print (files[f])
            #print(dst)
            shutil.copyfile(src, dst)
            if df!=None:
                dataset = dataset.append({'folder':'train',
                            'category':categories[x],
                            'file':files[f]
                            },ignore_index=True)

        for f in range(train_num, val_num):
            src = os.path.join(ogdata_dir + '/{}'.format(categories[x]), files[f])
            dst = os.path.join(validation_dir + '/{}'.format(categories[x]), files[f])
            #print (files[f])
            #print(src)
            #print(dst)
            shutil.copyfile(src, dst)
            if df!=None:
                dataset = dataset.append({'folder':'validation',
                            'category':categories[x],
                            'file':files[f]
                            },ignore_index=True)

        for f in range(val_num, len(files)):
            src = os.path.join(ogdata_dir + '/{}'.format(categories[x]), files[f])
            dst = os.path.join(test_dir + '/{}'.format(categories[x]), files[f])
            #print (files[f])
            #print(src)
            #print(dst)
            shutil.copyfile(src, dst)
            if df!=None:
                dataset = dataset.append({'folder':'test',
                            'category':categories[x],
                            'file':files[f]
                            },ignore_index=True)
    if df!=None:
        return dataset
    else:
        return None
    '''
    num_files = 0

    for x in range(0,len(categories)):
        files = os.listdir(ogdata_dir + '/{}'.format(categories[x]))
        num_files+=len(files)
    '''
