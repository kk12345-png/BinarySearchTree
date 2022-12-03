#! /usr/bin/python3
# NOTE: This Script is designed to work with Python 3.x version

# Selection sort method to sort array
def selectionSort(array, size):
    #Loop over the index numbers of the array
    for step in range(size):
        #Store first index value in a new variable min_index
        min_index = step
        #Then loop over rest of the index numbers and for each index, check value at that index in the array
        #and compare it with that of the min_index . If its less than value at min_index, if its lesser , then assign that index number to min_index
        for i in range(step + 1, size):
            # select the minimum element in each loop
            if array[i] < array[min_index]:
               min_index = i

        # put min at the correct position
        (array[step], array[min_index]) = (array[min_index], array[step])

# Method to Calculate Photographer Idle Time
def getPhotographerIdleTime(products):
    #Declare three variables as counters for idleTime, Staging Time and PhotoShoot Time. Also initialize variable i with value 0
    idleTime = 0
    staging_time = 0
    photo_time = 0
    i = 0
    #Now, loop over array . Update the staging time and photo time in each loop by adding the value in current loop to previous value
    while i < len(products):
        staging_time += products[i][0]
        photo_time += products[i][1]
        #For the first product in array, the idle Time is equal to staging time, as photo shoot requires at least one product to be staged
        if i == 0:
            idleTime += staging_time
        else:
            #If current value of photo shoot time is less than that of staging time , it means photographer has to wait till staging of next product is complete.
            if photo_time < staging_time:
                idleTime += staging_time - photo_time
        i += 1
    return idleTime

if __name__ == "__main__":
    #Read from Input file
    inputFile = open('InputPS19Q2.txt','r')
    lines = inputFile.readlines()
    #Check if there is data for at least one product in the input file
    if len(lines) > 0:
        #Create three lists for product name, staging time and photo time
        product_names = list(map(lambda x:x.strip() , lines[0].split(':')[1].strip().split('/')))
        staging_time = list(map(lambda x:int(x.strip()) , lines[1].split(':')[1].strip().split('/')))
        photo_time = list(map(lambda x:int(x.strip()) , lines[2].split(':')[1].strip().split('/')))
        #Close the Input file
        inputFile.close()
        #Initilize an empty array
        arr = []
        #Check if the number of items for product names, staging time and photo time is equal . If not exit the code with error
        if len(product_names) == len(staging_time) and len(product_names) == len(photo_time):
            # Loop over the product_names array and append tuple to the array arr with each tuple consisting of
            # (staging time, photo shoot time, product name) for each element.
            for i in range(len(product_names)):
                arr.append((staging_time[i],photo_time[i],product_names[i]))
        else:
            raise Exception("Exiting the program as either number of products is not matching either with the values provided in staging or that provided in photo time")
            exit(1)

        #Apply Selection sort method for array arr
        selectionSort(arr, len(arr))
        #Get idle time by calling method getPhotographerIdleTime() on array arr
        idleTime = getPhotographerIdleTime(arr)

        #Maximum time for Photoshoot is Total Photo Shoot time plus the Photographer Idle time.
        maxTime = idleTime + sum(photo_time)

        # Loop over the array and store the product names in sequence of array with comma separator
        productSeq = ''
        for item in arr:
            productSeq += item[2] + ','

        #Form the Output message thats going to be written to Output file
        outputMsg = ''
        outputMsg += 'Product Sequence: %s \n'%(productSeq[:-1]) # productSeq[:-1] prints the product sequence erasing the last comma
        outputMsg += 'Total time to complete photoshoot: %s minutes \n'%(maxTime)
        outputMsg += 'Idle time for Xavier: %s minutes'%(idleTime)

        # Create an Output file and write the output in desired format
        outputFile = open('OutputPS19Q2.txt','w+')
        outputFile.write(outputMsg)
        outputFile.close()
    else:
        #Exit the code , if either input file is empty or not in prescribed format
        raise Exception("Exiting Code with Error as either the input file is empty or its not in prescribed format")
        exit(1)


