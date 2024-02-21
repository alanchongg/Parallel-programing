from PIL import Image #find and open the image
import os #find the files i want to edit, split the name and the file type
import pilgram #apply filter
import time #keep track of process time
import multiprocessing as mp 

filters=['_1977', 'aden', 'brannan', 'brooklyn', 'clarendon', 'earlybird', 'gingham', 'hudson', 'inkwell', 'kelvin', 'lark', 'lofi',
         'maven', 'mayfair', 'moon', 'nashville', 'perpetua', 'reyes', 'rise', 'slumber', 'stinson', 'toaster', 'valencia', 'walden', 'willow', 'xpro2']

def filterimg (f):
    #go thru the folder
    for i in os.listdir('.'):
        #find all jpg files, filter them and save
        if i.endswith('.jpg'):
            img = Image.open(i)
            fname, fext= os.path.splitext(i)
            fn = getattr(pilgram, f)
            fn(img).save('p_filtered/{}_{}.png'.format(f, fname))         
            print('filtered image {} with {}'.format(fname, f))

def main ():
    pool=mp.Pool()
    ans=pool.map(filterimg, filters)  

if __name__=="__main__":
    startt=time.time()
    main()
    endt=time.time()
    print('Time taken for parallel processing', round(endt-startt,2), 'seconds')
