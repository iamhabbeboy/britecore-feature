from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABb6aK69m_M5c9_mDaf8fEaM5eXjVbkiJQnMORlKk1VQPIBjG0BPZNM4NCtaMGNSk7Bw1__-w7MKxIPBpkHPW0lHpCOoGD_IIAtGOx-acRZuQ1CtERpP8q8APIsUq_f6y1_vJ1fv2Gnv_Ul3_17hEwljcKQiOwtRsdl9Dw5m1FkuQKnzDLQCbJNwSYXHP6Ac3gRSj0-'


def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
