#!/bin/bash

# Modified PartIDs for Fall 2018 Coursera LE MOOC
MODULE1_GRADER_PART_ID="QL7c2"
MODULE2_GRADER_PART_ID="7YfGm"
MODULE3_GRADER_PART_ID="xa0LG"
MODULE4_GRADER_PART_ID="EP2fk"
MODULE5_GRADER_PART_ID="TMKNf"
MODULE6_GRADER_PART_ID="Bp0aI"
MODULE7_GRADER_PART_ID="IqhqT"
MODULE8_GRADER_PART_ID="V4QmL"

#for i in {1..8}
for i in {1..1}
do
  if [ "$i" == 1 ]; then
    PART_ID="$MODULE1_GRADER_PART_ID"
  elif [ "$i" == 2 ]; then
    PART_ID="$MODULE2_GRADER_PART_ID"
  elif [ "$i" == 3 ]; then
    PART_ID="$MODULE3_GRADER_PART_ID"
  elif [ "$i" == 4 ]; then
    PART_ID="$MODULE4_GRADER_PART_ID"
  elif [ "$i" == 5 ]; then
    PART_ID="$MODULE5_GRADER_PART_ID"
  elif [ "$i" == 6 ]; then
    PART_ID="$MODULE6_GRADER_PART_ID"
  elif [ "$i" == 7 ]; then
    PART_ID="$MODULE7_GRADER_PART_ID"
  elif [ "$i" == 8 ]; then
    PART_ID="$MODULE8_GRADER_PART_ID"
  else
    # Exiting with status 1. Coursera will expose these errors to 
    # instructors via a dashboard.
    # Learner will be prompted to try again after some time and the 
    # grader is under maintenance.
    echo "No PartId matched!" 1>&2
    exit 1
  fi

  #cp shared/submissions/m"$i"_assignment.ipynb shared/submissions/assignmenti_low.ipynb
  #make sure local shared/submissions/assignmenti_low.ipynb exists
  sudo courseraprogramming grade local accy577_grader shared/submission partId "$PART_ID"
done


