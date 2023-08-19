#!/bin/bash

# Fetch the HTML source of the page
html_source=$(curl -s https://www.kernel.org)

# Extract the line containing the stable version
stable_line=$(echo "$html_source" | grep -A1 '<td>stable:</td>')

# Extract the version number from the line
stable_version=$(echo "$stable_line" | grep -oP '(?<=<strong>)[^<]+')

echo "$stable_version"
