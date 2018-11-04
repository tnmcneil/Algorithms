# Theresa McNeil
# U09757615
# CS 330 Algorithms
# Homework 2 Problem 4

def schedule():

            # input: jobs.csv contains comma separated pairs of weights
            # and times for each job with one pair per line

            # output: list of the most optimal order in which jobs should be executed

            # read the jobs.csv file into jobsList with each value
            # as (w, t)

            # create empty list to store info on each job
            # in particular: the weight, the time, and the ratio of weight to time
            
            jobsList = []

            import csv
            # reading takes O(n) time (given on Piazza)
            with open('jobs.csv', 'r') as f: 
                        reader = csv.reader(f)
                        for job in reader:
                                    # needed to remove white space
                                    if job:
                                                weight = int(job[0])
                                                time = int(job[1])
                                                # computing ratio takes O(n)
                                                jobRatio = float(weight/time)
                                                jobsList.append([jobRatio, weight, time])

            # make hard copy of jobsList to reference later to preserve order
            
            original = list(jobsList)

            # sort the list in descending order of the ratio of weight to time
            # sorting takes O(nlogn)
            
            jobsList.sort(reverse = True)

            # create a list to hold the order in which each job should be run
            # done by checking the index of each job in the sorted order from the
            # original list so we refer to the jobs input by user

            # takes O(n)
            
            jobOrder = []
            for job in jobsList:
                        jobOrder.append(original.index(job))

            # return optimal order

            print(jobOrder)

            # total run time: O(n) + O(n) + O(nlogn) + O(n) == O(nlogn)
