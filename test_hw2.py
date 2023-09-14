import subprocess
from Sem_2 import checkout

folderin = "/home/user/tst"
folderout = "/home/user/test"
folderext = "/home/user/folder1"
foldersrc = "/home/user/folder2"


def test_step1():
    assert checkout(f"cd {folderin}; 7z a {folderout}/arx2", "Everything is Ok"), "test1 FAIL"


def test_step2():
    assert checkout(f"cd {folderout}; 7z e arx2.7z -o{folderext} -y", "Everything is Ok"), "test2 FAIL"


def test_step3():
    assert checkout(f"cd {folderout}; 7z t arx2.7z", "Everything is Ok"), "test3 FAIL"


def test_step4():
    assert checkout(f"cd {folderout}; 7z d arx2.7z", "Everything is Ok"), "test4 FAIL"


def test_step5():
    assert checkout(f"cd {folderin}; 7z u {folderout}/arx2.7z", "Everything is Ok"), "test5 FAIL"


# Задание 1.
#
# Условие:
# Дополнить проект тестами,
# проверяющими команды вывода списка файлов (l) и разархивирования с путями (x).

def test_hw_1_1():
    assert checkout(f"cd {folderout}; 7z l arx2.7z", "Listing archive: arx2.7z"), "test6 FAIL"


def test_hw_1_2():
    assert checkout(f"cd {folderout}; 7z x arx2.7z -o{folderext}", "Everything is Ok"), "test7 FAIL"


# *Задание 2. *
#
# • Установить пакет для расчёта crc32
# sudo apt install libarchive-zip-perl
# • Доработать проект, добавив тест команды расчёта хеша (h).
# Проверить, что хеш совпадает с рассчитанным командой crc32.

def test_hw_2():

    file_to_hash = "example.txt"
    cmd = f"cd {foldersrc}; 7z h {file_to_hash}"
    result = checkout(cmd, "CRC32 =")
    if result and "CRC32 =" in result.stdout:
        crc32_value = result.stdout.split("CRC32 =")[1].strip()

        import zlib
        with open(f"{foldersrc}/{file_to_hash}", "rb") as file:
            file_contents = file.read()
            calculated_crc32 = zlib.crc32(file_contents) & 0xFFFFFFFF
        if crc32_value == str(calculated_crc32):
            print("test8 PASS")
        else:
            print("test8 FAIL: CRC32 mismatch")
    else:
        print("test8 FAIL: Command execution failed")


test_hw_2()

