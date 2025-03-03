#!/usr/bin/bash

for file in state.py city.py amenity.py place.py review.py; do 
    class_name=$(echo ${file%.py} | tr '[:lower:]' '[:upper:]' | cut -c1)$(echo ${file%.py} | cut -c2-)
    echo "class $class_name:" > "$file"
    echo "  \"\"\"Model class for ${file%.py}\"\"\"" >> "$file"
    echo "  pass" >> "$file"
done



