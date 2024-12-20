class Tasks :
    @staticmethod
    def divisors() :
        """ method prints to console all divisors of input number """
        print("Enter a positive integer:")
        try:
            n = int(input())
            [print(f"{i} is a factor of {n}") for i in range(1, n + 1) if n % i == 0]
        except ValueError:
            print("invalid input.Please enter numeric values ")


    @staticmethod
    def enrollment_stats(input_list):
        """Extracts and returns students and tuition fees as two separate lists from input list of lists
           2nd element of sublist is student numbers 3rd element is tuition fees"""
        enrollment_values, tuition_fees = zip(*[(sublist[1], sublist[2]) for sublist in input_list])
        return list(enrollment_values),list(tuition_fees)

    @staticmethod
    def mean(lst):
        return sum(lst)/len(lst)

    @staticmethod
    def median(lst):
        n = len(lst)
        lst.sort()
        if n % 2 == 0:
            return (lst[n//2 -1]+lst[n//2])/2
        else:
            return lst[(n+1)//2 -1]
    @staticmethod
    def is_prime(n):
        k =sum( [1 for i in range(1, int(n **0.5)) if n % i == 0])+1
        if k>2 :
           return  False
        else :
            return True
#Task3
Tasks.divisors()

# task4
universities = [
        ['California Institute of Technology', 2175, 37704],
        ['Harvard', 19627, 39849],
        ['Massachusetts Institute of Technology', 10566, 40732],
        ['Princeton', 7802, 37000],
        ['Rice', 5879, 35551],
        ['Stanford', 19535, 40569],
        ['Yale', 11701, 40500]
         ]

students, tuition = Tasks.enrollment_stats(universities)
print(f"Total students: {sum(students):,}")
print(f"Total tuition: $ {sum(tuition):,}")
print()
print(f"Student mean: {round(Tasks.mean(students), 2):,} ")
print(f"Student median: {Tasks.median(students):,}")
print()
print(f"Tuition mean: $ {round(Tasks.mean(tuition), 2):,}")
print(f"Tuition median: $ {Tasks.median(tuition):,}")

# task5
print(Tasks.is_prime(37))
# Output: True