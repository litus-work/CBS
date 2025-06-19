import threading
import os
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(threadName)s: %(message)s',
    datefmt='%H:%M:%S'
)

wow_found_event = threading.Event()
file_name = "example.txt"

def watch_file():
    while not wow_found_event.is_set():
        if not os.path.exists(file_name):
            logging.info(f"Файл '{file_name}' не найден. Ожидание...")
            time.sleep(5)
            continue

        with open(file_name, 'r', encoding='utf-8') as f:
            contents = f.read()
            if "Wow!" in contents:
                logging.info("Обнаружено 'Wow!' в файле.")
                wow_found_event.set()
            else:
                logging.info("'Wow!' не найден в файле. Повтор через 5 секунд.")
                time.sleep(5)

def delete_on_event():
    logging.info("Ожидание события...")
    wow_found_event.wait()
    try:
        os.remove(file_name)
        logging.info(f"Файл '{file_name}' удалён.")
    except FileNotFoundError:
        logging.warning(f"Файл '{file_name}' уже был удалён.")

def main():
    thread1 = threading.Thread(target=watch_file, name="Watcher")
    thread2 = threading.Thread(target=delete_on_event, name="Deleter")

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    logging.info("Программа завершена.")

main()
