import sys
def analyze_cat__log(cat_file):
    try:
        with open(cat_file, 'r') as f:
            total_no_time_correct_cat_entered = 0
            intruder_cat_doused = 0
            total_time_correct_cat_spend = 0
            visit = []
            
            for line in f:
                if line == 'END':
                    break
                else:
                    part = line.split(',')
                    cat_name=part[0] 
                    entry_time=int(part[1])
                    exit_time =int(part[2])
                if cat_name == 'OURS':
                    total_no_time_correct_cat_entered += 1
                    a= exit_time - entry_time
                    total_time_correct_cat_spend += a
                    visit.append(a)
                elif cat_name=='THEIRS':
                    intruder_cat_doused += 1

            if total_no_time_correct_cat_entered == 0:
                print("No entries for the designated cat in the log file.")
            else:
                average_duration = sum(visit) / total_no_time_correct_cat_entered
                longest_duration = max(visit)
                shortest_duration = min(visit)
                print("\nLog File Analysis")
                print("==================")
                print(f"Cat Visits: {total_no_time_correct_cat_entered}")
                print(f"Other Cats: {intruder_cat_doused}")
                print(f"Total Time in House: {total_time_correct_cat_spend // 60} Hours, {total_time_correct_cat_spend % 60} Minutes")
                print(f"Average Visit Length: {average_duration:.0f} Minutes")
                print(f"Longest Visit: {longest_duration} Minutes")
                print(f"Shortest Visit: {shortest_duration} Minutes")

    except FileNotFoundError:
        print(f"Cannot open  \"{cat_file}\"!")

if len(sys.argv) < 2:
    print("Missing command line argument!")
else:
    file = sys.argv[1]
    analyze_cat__log(file)

