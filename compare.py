import argparse
import ast


#функция для нахождения расстояния Левенштейна между двумя строками 
def get_lev_dist(str_1, str_2):
    n, m = len(str_1), len(str_2)
    if n > m:
        str_1, str_2 = str_2, str_1
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if str_1[j - 1] != str_2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)
    
    return str(float(current_row[n]) / m)


#парсер аргументов, передаваемых в консоли
parser = argparse.ArgumentParser()
parser.add_argument('input', type=str)
parser.add_argument('scores', type=str)
args = parser.parse_args()
input_file_path, scores_file_path = args.input, args.scores


with open(scores_file_path, 'w') as scores_file:
    with open(input_file_path, 'r') as input_file:
        for line in input_file:
            splitted_line = line.split()
            file_name1, file_name2 = splitted_line[0], splitted_line[1]
            with open(file_name1) as file1:
                text_file1 = file1.read()
            with open(file_name2) as file2:
                text_file2 = file2.read()
            scores_file.write(get_lev_dist(text_file1, text_file2) + '\n')