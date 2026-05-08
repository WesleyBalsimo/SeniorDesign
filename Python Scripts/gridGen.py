#import machine
#from machine import Pin
#import functions
#import calibration


def main():
    matrix = []

    with open('C:\\Git Projects\\SeniorDesign\\Other Files\\SD403_SP26_07 (gridview).csv', 'r') as file:
        for line in file:
            row = line.strip().split(',')
            row = [str(i) for i in row]
            matrix.append(row)
    
    x = 0
    y = 0
    for row in matrix:
        x += 1
        for string in row:
            y += 1

    print('x: ' + str(x))
    print('y: ' + str(y))
    #calibration.sizeX
    #calibration.sizeY


if __name__ == "__main__":
    main()