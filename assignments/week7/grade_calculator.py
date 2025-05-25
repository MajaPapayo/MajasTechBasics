from sys import argv
import csv
import random

# maximum Score for a task
MAX_SCORE = 3
# dictionarie of student
items = []
# list week 1 - 13, skipping 6
week_list = [f"week{i}" for i in range(1, 14) if i != 6]

# Step 1
def read_csv(filename):
    global items
    try:
        with open(filename, newline='') as f:
            reader = csv.DictReader(f)
            items = [row for row in reader]
    except FileNotFoundError:
        print(f"📢ERROR: CSV file of the name '{filename}' not found")
    except PermissionError:
        print(f"📢ERROR: No permission to access file of the name '{filename}'!")

# Step 2
def populate_scores(filename):
    global items
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        items = [row for row in reader]

    for item in items:
        for x in week_list:
            score = item.get(x, "").strip()
            if score == "":
                item[x] = str(random.randint(0, MAX_SCORE))
            else:
                item[x] = score

# Step 3
def calculate_all():
    for item in items:
        scores = []
        for week in week_list:
            value = item.get(week, '').strip()
            if value.isdigit():
                scores.append(int(value))
        item["Total Points"] = calculate_total(scores)
        item["Average Points"] = calculate_average(scores)

def calculate_total(scores):
    return min(sum(sorted(scores, reverse=True)[:10]), 30)

def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return round(sum(scores) / len(scores), 2)

# Save updated CSV
def write_csv(new_filename):
    if not items:
        print(" 📢  No data to print")
        return
    fieldnames = list(items[0].keys())
    with open(new_filename, mode='w', newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(items)
    print("Updated CSV saved as:", new_filename)

# Bonus
def print_analysis():
    streams = {"A": [], "B": []}
    week_totals = {x: [] for x in week_list}

    for item in items:
        stream = item.get("Stream", "").strip().upper()
        try:
            avg = float(item["Average Points"])
        except:
            avg = 0
        if stream in streams:
            streams[stream].append(avg)

        for w in week_list:
            try:
                score = int(item.get(w, 0))
            except:
                score = 0
            week_totals[w].append(score)

    print("\naverage points by stream:")
    for stream, vals in streams.items():
        avg = round(sum(vals) / len(vals), 2) if vals else 0
        print(f"  stream {stream}: {avg} points")

    print("\naverage points per week:")
    for w in week_list:
        vals = week_totals[w]
        average = round(sum(vals) / len(vals), 2) if vals else 0
        print(f"  {w}: {average} points")

if __name__ == "__main__":
    script, filename = argv

    print("Open file:", filename)

    read_csv(filename)
    populate_scores(filename)
    calculate_all()

    user_name = input("Please enter your name : ")
    newname = filename.split(".")[0] + "_calculated_by_" + user_name + ".csv"

    write_csv(newname)
    print("New file written:", newname)

    print_analysis()
