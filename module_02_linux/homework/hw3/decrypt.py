import sys
import re


def decrypt(encryption: str) -> str:
    while '.' in encryption:
        if '..' in encryption:
            pattern = r'[a-zA-Zа-яА-Я -.0-9][\.]{2}'
            match = re.search(pattern=pattern, string=encryption)
            encryption = encryption.replace(match.group(0), '')
        else:
            encryption = encryption.replace('.', '')

    return encryption


if __name__ == '__main__':
    data: str = sys.stdin.read()
    decryption: str = decrypt(data)
    print(decryption)
