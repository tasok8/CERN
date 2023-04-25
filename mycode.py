import re
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", default="./logs/ssl-access.log.2", help="Path to input file")
parser.add_argument("-o", "--output", default="./outputs/output.csv", help="Path to output file")
args = parser.parse_args()

pattern = r"/root_v(\d+\.\d+\.\d+)\.(Linux|macos|win32|win64|source)"

data = []

print("Using input file:", args.input)
print("Using output file:", args.output)


with open(args.input, "r") as log_file:
    for line in log_file:
        if 'GET' in line: 
            match = re.search(pattern, line)
            if match:
                version = match.group(1)
                platform = match.group(2)
                date = re.search(r'\[(.*?)\]', line).group(1)
                user_agent = re.search(r'"(.+?)"', line).group(1)
                if 'bot' not in user_agent.lower() and 'spider' not in user_agent.lower() and 'crawl' not in user_agent.lower():
                    data.append([date, version, platform])

with open(args.output, "w") as output_file:
    writer = csv.writer(output_file)
    writer.writerow(["Date", "Version", "Platform"])
    writer.writerows(data)
