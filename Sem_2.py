import subprocess


def checkout(cmd, text, timeout=30):
    try:
        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8', timeout=timeout)
        return result
    except subprocess.TimeoutExpired:
        return None


def checkout_negative(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    # print(result.stdout)
    if (text in result.stdout or text in result.stderr) and result.returncode != 0:
        return True
    else:
        return False

