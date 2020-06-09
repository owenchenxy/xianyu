filepath = './metaG.gff'
resultpath = './result.gff'

result = list()
with open(filepath) as f:
    for line in f.readlines():
        arr = line.split()
        if 'NODE' not in arr[0]:
            result.append(line)
            continue
        try:
            arr[8] = "ID="+arr[0]
        except Exception:
            result.append(line)
            continue
        result.append(' '.join(arr)+"\n")

with open(resultpath,'w') as f:
    f.writelines(result)

print('Task Done!')
