filepath = './metaG.gff'
resultpath = './result.gff'

result = list()
with open(filepath) as f:
    for line in f.readlines():
        columns = line.split(';')
        first_column = columns[0]
        arr = first_column.split("\t")
        if 'NODE' not in arr[0]:
            result.append(line)
            continue
        try:
            arr[8] = "ID="+arr[0]
        except Exception:
            result.append(line)
            continue

        columns[0] = "\t".join(arr)
        line = ';'.join(columns)
        result.append(line)

with open(resultpath,'w') as f:
    f.writelines(result)

print('Task Done!')
