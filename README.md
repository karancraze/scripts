# scripts
My Custom Scripts for Data Science

## dl_images_setup.py - Used for setting up images folder structure for deeplearning projects
### Usage
Used for just shuffling the data in train, test and validation splits
### Syntax
- **shuffle_img('ogdata', 'data', 0.6, 0.2, 0.2)**  
1st argument is original folder where are images are already into there respective class folders.  
2nd argument is the folder in which they will be split into train test and validation split.  
3rd, 4th, 5th arguments are train, test, validation splits respectively.  

- **df = shuffle_img('ogdata', 'data', 0.6, 0.2, 0.2, 'df')**  
If you use the above command it will setup the folder structure as well as return a dataframe consisting of file names, folder it was sent to and the category it belongs to.  
Useful when you need to track the file.
