#import machine
#from machine import Pin
#import functions
#import calibration


def main():
    matrix = []

    with open('Other Files\\SD403_SP26_07 (gridview).csv', 'r') as file:
        for line in file:
            row = line.strip().split(',')
            row = [str(i) for i in row]
            matrix.append(row)
    
    x = 0
    y = 0

    tempSize0 = 0
    tempSize = 0
    
    #Get the max size of the grid by checking each row/column to the biggest found so far
    for row in matrix:
        tempSize0 += 1
        if tempSize0 > x:
            x = tempSize0
        for cell in row:
            tempSize += 1
            if tempSize > y:
                y = tempSize
        tempSize = 0
    tempSize0 = 0

    print('x: ' + str(x))
    print('y: ' + str(y))
    #calibration.sizeX
    #calibration.sizeY


if __name__ == "__main__":
    main()