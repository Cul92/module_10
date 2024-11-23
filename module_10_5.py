import time
import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        line = file.readline()
        while line:
            all_data.append(line)
            line = file.readline()


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    end_time = time.time()
    print(f"Время выполнения линейного вызова: {datetime.fromtimestamp(end_time - start_time).strftime('%H:%M:%S.%f')}")
    start_time = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    print(
        f"Время выполнения многопроцессного вызова: {datetime.fromtimestamp(end_time - start_time).strftime('%H:%M:%S.%f')}")
