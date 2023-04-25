import re
import csv
import argparse

pattern = r"/root_v(\d+\.\d+\.\d+)\.(Linux|macos|win32|win64|source)"

data = []

with open("./logs/ssl-access.log.2", "r") as log_file:
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

with open("./outputs/output.csv", "w") as output_file:
    writer = csv.writer(output_file)
    writer.writerow(["Date", "Version", "Platform"])
    writer.writerows(data)
