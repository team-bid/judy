import RPi.GPIO as GPIO
import time
import datetime
import sys
import csv

COMMA = ','
QUOTE = '"'
TRUE_BIT = '1'
FALSE_BIT = '0'

INPUT_YES = 18
INPUT_NO = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(INPUT_YES, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(INPUT_NO, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def read_bitmaps(file_name):
    bitmap_to_item = {}
    with open(file_name) as csvfile:
        reader = csv.reader(csvfile, delimiter = COMMA, quotechar = QUOTE)
        for line in reader:
            item_name, bitmap = line
            bitmap_to_item[bitmap] = item_name
    return bitmap_to_item

def get_bit(answer):
    if answer is 'y':
        return TRUE_BIT
    return FALSE_BIT

def get_response():
    if GPIO.input(INPUT_YES) == 0:
        return TRUE_BIT
    elif GPIO.input(INPUT_NO) == 0:
        return FALSE_BIT
    return COMMA

def main(bitmap_file_name):
    bitmap_to_item = read_bitmaps(bitmap_file_name)
    
    answer = ''
    current_bitmap = 'X'

    # ask root question
    start = time.time()
    print('QUESTION: %s' % bitmap_to_item[current_bitmap])

    while True:
        while get_response == COMMA:
            answer = get_response()
        current_bitmap += answer

        if current_bitmap in bitmap_to_item:
            if '?' in bitmap_to_item[current_bitmap]:
                print('QUESTION: %s' % bitmap_to_item[current_bitmap])
            else:
                print('    ITEM: %s' % bitmap_to_item[current_bitmap])
                end = time.time()
                print('\n---- Experimenter\'s Use ----')
                print(' TREE FILE: %s' % bitmap_file_name)
                print('TIME TAKEN: %.3f SECONDS' % (end-start))
                break
    return

main(sys.argv[1])
