# Build low engagement assignments for release on Coursera MOOC ACCY577

# Major steps:

1. Create assignments with nbgrader, generate release(generate_assignment)
2. Create programming assignment on Coursera, get graded_item_id from URL. ie. 5FK0X (/programming/5FK0X?versionId=..), partId and file name(ie. m1_assignment.ipynb)
3. Create notebook assignment, get launchid from URL, ie. w5fdK(.../notebook/w5fdK/launcher?)
4. Modify assignment notebook metadata, add coursera block including course_slug, graded_item_id and launch_item_id.
5. Run nbgrader generate_assignment Module1 --force to create release version.
6. Create nbgrader_config.py
7. Create execute_grader.sh, update partID, generate_assignment to create gradebook.db, copy submitted assignment from coursera to nbgrader env.
8. Create exporter.py
9. Create Dockerfile, add nose, nbgrader on top of jupyter/scipy-notebook tag, create grader dir, copy source assignment
10. Generate docker image "sudo docker build -t accy577_grader .", folder need to have:
    - Dockerfile
    - execute_grader.sh
    - exporter.py
    - nbgrader_config.py
    - source(only keep low assignment in each module)
11. Run test.sh to test
    - Make sure shared/submissions/assignmenti_low.ipynb exists in current folder
12. Build and Upload docker tar file to coursera program assignment

# Refresh notebook on coursera
1. Upload new notebook from Instructor workspace
2. Open the file with Learner's view, rename file
3. In the url, add ?forceRefresh=true at the end and reload page
4. Delete renamed file

-----
# build docker image
# in iMSA577_Redesign/coursera_nbgrader_setup/build_grader/ run:
sudo docker build -t accy577_grader .
# list docker image
docker image list
#delete docker image
docker rmi dockerid
# build tar file(not needed)
sudo docker save accy576_grader -o accy576_grader.tar

# test
# Set python 2.7 env
$ conda create -n p27 python=2.7
$ conda activate p27

# Install courseraprogramming
$ git clone https://github.com/coursera/courseraprogramming
# Need to run following to install in p27 every time
$ cd courseraprogramming/
$ python setup.py develop
$ pip install -r test_requirements.txt

# put /Users/lindenlu/uiuc/Spring_2019/iMSA577_Redesign/coursera_nbgrader_setup/shared/submission to docker file sharing

sudo ./test.sh






Grader output:
================================================================================
{"fractionalScore": 1.0, "feedback":"Congrats! All test cases passed!"}
================================================================================

Now upload assignments in the release directory to Coursera JupyterHub server

- Stop Server
- Logout
- Publish Workspace
- Publish  and return to course

Next, upload autograder and assign it to assignments

Install [courseraprogramming](https://github.com/coursera/courseraprogramming#grade)

sudo pip install courseraprogramming

-----

ACCY577:
course-slug: machine-learning-accounting-python
module 1 itemid: 1nckY launchid:QL7c2
module 2 itemid: zCbq1 launchid:7YfGm
module 3 itemid: HvbED launchid:xa0LG
module 4 itemid: lKTm1 launchid:EP2fk
module 5 itemid: bgKXX launchid:TMKNf
module 6 itemid: nMM73 launchid:Bp0aI
module 7 itemid: 5mKNj launchid:IqhqT
module 8 itemid: 0806u launchid:V4QmL


# Copy files to coursera
Run ./copy_files.sh to create zip files for lesson and assignments
Upload zip files to coursera through instructor Workspace
Open a new notebook and run following.
Remove existing folder first with !rm -r Assignments/Lessons if necessary.
```
import zipfile as zf
files = zf.ZipFile("Lessons.zip", 'r')
files.extractall('.')
files.close()

files = zf.ZipFile("Assignments.zip", 'r')
files.extractall('.')
files.close()
```
# if create readonly folder, delete coursera part in assignment notebook metadata.
