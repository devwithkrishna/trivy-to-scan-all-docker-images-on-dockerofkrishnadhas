#! /bin/bash

# Read the JSON file and extract the image names
images=$(cat docker_images_details_dockerofkrishnadhas.json | jq -r '.[]')

#  Iterate over each image
for image in $images
  do
      echo $image
      start_time=$(date +%s)  # Get the start time in seconds

      echo "Scanning started for image: $image at $(date)"

      # Run the Docker scanner command (replace with your actual command)
      # docker scanner_command $image
      sleep 5  # Simulate scanning process with a sleep command

      end_time=$(date +%s)  # Get the end time in seconds
      duration=$((end_time - start_time))  # Calculate the duration in seconds

      # Print the end time and duration
      echo "Scanning ended for image: $image at $(date)"
#      echo "Duration for image $image: $duration seconds"
  done