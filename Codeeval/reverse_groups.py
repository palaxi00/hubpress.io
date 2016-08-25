import sys
import itertools

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        stringe = test.strip()
        list1 = [int(i) for i in stringe.split(";")[0].split(",")]
        list2=[]
        howmany = int(stringe.split(";")[1])
        for i in range(0,len(list1),howmany):
            mini = list(list1[i:howmany+i])[::-1]
            if len(mini) == howmany:
                list2.append(mini)
            else:
                list2.append(list(list1[i::]))
        total = [str(i) for i in (list(itertools.chain.from_iterable(list2)))]
        print (",".join(total))