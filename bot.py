import random

def jenissampah(pertanyaan):
    pertanyaan = int(input('sampah apa yang ingin anda tahu jenisnya?'))
    if pertanyaan=='apa jenis sampah plastik':
        choices = ['sampah plastik merupakan jenis sampah anorganik', 'jenisnya adalah anorganik']
        print(random.choice(choices))

    elif pertanyaan=='apa jenis sampah sisa makanan':
        print('sisa makanan merupakan sampah jenis sampah organik')
