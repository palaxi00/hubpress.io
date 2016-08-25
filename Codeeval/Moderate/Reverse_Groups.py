import sys
import itertools

with open(sys.argv[1], 'r') as test_cases:
    #GET THE FILE
    for test in test_cases:
        #ITERATION OVER ALL LINES
        stringe = test.strip()
        #MAKE A VARIABLE EQUAL TO THE LINE AT THE ITERATION
        list1 = [int(i) for i in stringe.split(";")[0].split(",")]
        # stringe.split(";")[0] EQUALS TO THE LIST OF NUMBERS NEEDED TO SOLVE THE PROBLEM
        #.split(",") TO SAVE ALL NUMBERS IN A LIST OF STRINGS
        #[int(i) for i in stringe.split(";")[0].split(",")] CREATE A LIST PARSING ALL STRINGS IN THE LAST LIST TO INTEGERS
        list2=[]
        #EMPTY LIST FOR SAVING REVERSED SUB LISTS
        howmany = int(stringe.split(";")[1])
        #GET THE LAST ITEM IN THE test VARIABLE, THIS IS THE LENGTH OF THE SUBSTRINGS TO CREATE
        for i in range(0,len(list1),howmany):
            mini = list(list1[i:howmany+i])[::-1]
            if len(mini) == howmany:
                list2.append(mini)
            else:
                list2.append(list(list1[i::]))
        total = [str(i) for i in (list(itertools.chain.from_iterable(list2)))]
        print (",".join(total))
