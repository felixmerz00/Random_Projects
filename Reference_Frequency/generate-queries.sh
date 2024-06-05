# This script generates the phrases I want to count, i.e., all definitions, propositions, remarks, examples, and exercises.

# Set default "." as the default char for comma in floats
export LC_NUMERIC="en_US.UTF-8"

# Clear file
> queries.txt

for j in $(seq 1 12); do
  for i in $(seq 1 26); do
    num=$(printf "$j.$i")
    printf "definition %s\nproposition %s\nremark %s\nexample %s\nexercise %s\n" $num $num $num $num $num >> queries.txt
  done
done


# archive
# for num in $(seq 1.01 0.01 1.26); do
# printf "definition %.2f\nproposition %.2f\nremark %.2f\nexample %.2f\nexercise %.2f\n" $num $num $num $num $num >> output.txt
# done
