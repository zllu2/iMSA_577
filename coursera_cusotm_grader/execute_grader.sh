#!/bin/bash

# Maintained by Linden Lu(zllu2@illinois.edu)

# Coursera deletes all environment variables set inside 'Dockerfile'.
# If any environment variables need to be set, they must be set
# inside a wrapper bash script.
export HOME=/grader

# Switch to the grader directory
cd /grader

# Unique Part Ids for each assignment part that will be graded using this grader.
# These are exposed in Coursera's authoring tools for each programming assignment part.

# Modified PartIDs(launchid) for Spring 2020 ACCY577 MOOC Assignment
MODULE1_GRADER_PART_ID="QL7c2"
MODULE2_GRADER_PART_ID="7YfGm"
MODULE3_GRADER_PART_ID="xa0LG"
MODULE4_GRADER_PART_ID="EP2fk"
MODULE5_GRADER_PART_ID="TMKNf"
MODULE6_GRADER_PART_ID="Bp0aI"
MODULE7_GRADER_PART_ID="IqhqT"
MODULE8_GRADER_PART_ID="V4QmL"

# Parse the command line arguments supplied by Coursera.
while [[ $# > 1 ]]
  do
    key="$1"
    case $key in
      partId)
        # Unique Id associated with the part which is being graded.
        PARTID="$2"
        shift
        ;;
      filename)
        # Original filename as uploaded by the learner.
        # Note: Coursera 'always' renames the submission to the suggested filename
        # as specified within the authoring UI.
        # This is an optional parameter and most of the graders don't end up using it.
        ORIGINAL_FILENAME="$2"
        shift
        ;;
    esac
  shift
done

# Use the parsed partId to know which part is being graded in the current run.
if [ "$PARTID" == "$MODULE1_GRADER_PART_ID" ]; then
  MODULE=Module1
  NOTEBOOK="m1_assignment.ipynb"
elif [ "$PARTID" == "$MODULE2_GRADER_PART_ID" ]; then
  MODULE=Module2
  NOTEBOOK="m2_assignment.ipynb"
elif [ "$PARTID" == "$MODULE3_GRADER_PART_ID" ]; then
  MODULE=Module3
  NOTEBOOK="m3_assignment.ipynb"
elif [ "$PARTID" == "$MODULE4_GRADER_PART_ID" ]; then
  MODULE=Module4
  NOTEBOOK="m4_assignment.ipynb"
elif [ "$PARTID" == "$MODULE5_GRADER_PART_ID" ]; then
  MODULE=Module5
  NOTEBOOK="m5_assignment.ipynb"
elif [ "$PARTID" == "$MODULE6_GRADER_PART_ID" ]; then
  MODULE=Module6
  NOTEBOOK="m6_assignment.ipynb"
elif [ "$PARTID" == "$MODULE7_GRADER_PART_ID" ]; then
  MODULE=Module7
  NOTEBOOK="m7_assignment.ipynb"
elif [ "$PARTID" == "$MODULE8_GRADER_PART_ID" ]; then
  MODULE=Module8
  NOTEBOOK="m8_assignment.ipynb"
else
  # Exiting with status 1. Coursera will expose these errors to instructors via a dashboard.
  # Learner will be prompted to try again after some time and the grader is under maintenance.
  echo "No PartId matched!" 1>&2
  exit 1
fi

# Copy the source file and run nbgrader assign.
cp -r /grader/source/"$MODULE" /grader/source/module
cd /grader
nbgrader generate_assignment module

# Copy the submission to corresponding directory in the nbgrader directory structure.
mkdir -p /grader/submitted/student/module
#cp /shared/submission/"$NOTEBOOK" /grader/submitted/student/module/assignment_low.ipynb
# We can assume there is only one notebook file in submission folder
cp /shared/submission/*.ipynb /grader/submitted/student/module/assignment_low.ipynb

# Run nbgrader
nbgrader autograde --assignment=module
nbgrader export --exporter=exporter.JsonExportPlugin

# Note: Nothing except Json object containing 'fractionalScore' and 'feedback' should be written
# to stdout.
cat grades.json
