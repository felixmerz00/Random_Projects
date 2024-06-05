# This file counts the phrases from the input_file in the search_file and 
# writes the result ordered by the phrase's frequency to a new text file.

> reference-frequency.txt

# Input file containing the phrases and file in which we will search for the phrases
# prod files
input_file="queries.txt"
search_file="script-clean.txt"

# smaller debug files
# input_file="queries-debug.txt"
# search_file="test-text.txt"

# Loop through each line in the input file
while IFS= read -r phrase; do
    # Count the occurrences of the phrase in the search file
    count=$(grep -oiwF "$phrase" "$search_file" | wc -l)
    # Append the phrase and count to the output file
    printf "%s,%d\n" "$phrase" "$count" >> reference-frequency.txt
done < "$input_file"

sort -t ',' -k2 -nr -o reference-frequency.txt reference-frequency.txt

# Notes about grep
# grep -oiwF [query] [file] | wc -l
# -o Print only the matched parts of a matching line, with each such part on a separate output line.
# -i Ignore casing
# -w Only look at whole words
# -F Treats search string as a fixed string (no regular expression interpretation) to increase performance
# | wc -l Count the lines from the output of the first command.
