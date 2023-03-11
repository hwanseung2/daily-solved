from collections import defaultdict

def solution(commands):
    answer = []
    cell = defaultdict()
    is_merged = defaultdict(list)

    for command in commands:
        command = command.split()
        cmd, arg = command[0], command[1:]
        if cmd == "UPDATE":
            if len(arg) == 3:
                r, c, value = arg
                r, c = int(r), int(c)
                if len(is_merged[(r,c)]) == 0:
                    cell[(r,c)] = value
                else:
                    cell[(r,c)] = value
                    for key in is_merged[(r,c)]:
                        cell[key] = value
            elif len(arg) == 2:
                value1, value2 = arg
                for key in cell.keys():
                    if cell[key] == value1:
                        cell[key] = value2
        elif cmd == "MERGE":
            arg = list(map(int, arg))
            r1, c1, r2, c2 = arg
            if (r1, c1) == (r2, c2):
                continue
            value1, value2 = cell.get((r1, c1)), cell.get((r2, c2))
            merged1, merged2 = is_merged[(r1,c1)] + [(r2,c2)], is_merged[(r2,c2)] + [(r1,c1)]
            merged = list(set(merged1) | set(merged2))
            for merge_key in merged:
                is_merged[merge_key] = merged

            if value1 == None and value2 != None:
                for key in is_merged[(r2,c2)]:
                    cell[key] = value2
            elif (value1 != None and value2 == None) or (value1 != None and value2 != None):
                for key in is_merged[(r1,c1)]:
                    cell[key] = value1
        
        elif cmd == "UNMERGE":
            r, c = arg
            r, c = int(r), int(c)
            value = cell.get((r,c))
            merged = [(r,c)] + is_merged[(r,c)]
            for merge_key in merged:
                if merge_key != (r,c):
                    cell[merge_key] = None
                else:
                    cell[merge_key] = cell.get(merge_key)
                is_merged[merge_key] = []
        elif cmd == "PRINT":
            r, c = arg
            r, c = int(r), int(c)
            if cell.get((r,c)) == None:
                answer.append("EMPTY")
            else:
                answer.append(cell.get((r,c)))
    return answer

print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))