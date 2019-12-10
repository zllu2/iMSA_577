#!/bin/bash
# create lesson and assignment folders to be uploaded to coursera
# to use, run ./copy_files.sh
# then upload zip files to coursra
# on courser, create a new notebook and run following code
#import zipfile as zf
#files = zf.ZipFile("Lessons.zip", 'r')
#files.extractall('.')
#files.close()

#files = zf.ZipFile("Assignments.zip", 'r')
#files.extractall('.')
#files.close()

rm -r Lessons
mkdir Lessons
cd Lessons
for i in {1..8}
do
  mkdir Module"$i"
  cp -R ../../lessons/Module"$i"/notebooks/* Module"$i"
  rm Module"$i"/m"$i"*.ipynb
done

cd ..
rm -r Assignments
mkdir Assignments
cd Assignments
mkdir release
cd release

for i in {1..8}
do
  mkdir Module"$i"
  cp -R ../../../assignments/release/Module"$i"/* Module"$i"
  rm Module"$i"/assignment_high.ipynb
done
cd ../..
zip -vr Lessons.zip Lessons/ -x "*.DS_Store"
zip -vr Assignments.zip Assignments/ -x "*.DS_Store"
rm -r Lessons
rm -r Assignments
