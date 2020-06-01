T=input('#TestCases')
cases=[]

for i in range(int(T)):
    N=0
    B=0
    test_case_line=input('#OfHouses Budget')

    test_case_line_list=test_case_line.split(' ')
    N=int(test_case_line_list[0])
    B=int(test_case_line_list[1])

    test_case_line2=input('NPricesOfEachHouse')
    A=test_case_line2.split(' ')
    A=[int(i) for i in A]
    A.sort()
    over_price=0
    number_of_Houses=0
    if A[0]<=B:
        for price in A:
            over_price+=price
            if over_price<=B:
                number_of_Houses+=1
    cases.append(number_of_Houses)

TestCase=1
for n in cases:
    print(f'Case #{TestCase}: {n}')
    TestCase+=1