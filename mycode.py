import re
import csv
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("inputfiles", default="./logs/ssl-access.log.2", help="Path to input file", nargs='+')
args = parser.parse_args()

pattern = r"/root_v(\d+\.\d+\.\d+)\.(Linux|macos|win32|win64|source)"

data = []

with open('outputs/all.csv', "w") as output_file:
    writer = csv.writer(output_file)
    writer.writerow(["Date", "Version", "Platform"])
    for inputfile in args.inputfiles:
        print(f"Processing {inputfile}")
        with open(inputfile, "r") as log_file:
            for line in log_file:
                if 'GET' in line:
                    line = line.strip() 
                    match = re.search(pattern, line)
                    if match:
                        version = match.group(1)
                        version = version.replace(".", "", 1)
                        platform = match.group(2)
                        date = re.search(r'\[(.*?)\]', line).group(1)
                        user_agent = re.findall(r'"(.+?)"', line)[2]
                        if 'bot' not in user_agent.lower() and 'spider' not in user_agent.lower() and 'crawl' not in user_agent.lower():
                            writer.writerow([date, version, platform])
