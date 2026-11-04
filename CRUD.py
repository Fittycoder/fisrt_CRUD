import sys

data_siswa = []

def tambah():
    nama_siswa = input('Masukkan nama siswa: ').capitalize()
    if not nama_siswa.isalpha():
        print('Nama tidak boleh berisikan angka!')
        return
    if any(siswa['nama'] == nama_siswa for siswa in data_siswa):
        print('Nama sudah ada, apakah anda tetap ingin menambahkan nama? (y/n)')
        if input == 'n':
            return
    while True:
        nisn_siswa = input('Masukkan NISN siswa: ')
        if len(nisn_siswa) <= 8 and nisn_siswa.isdigit():
            if any(siswa['nisn'] == nisn_siswa for siswa in data_siswa):
                print('NISN sudah ada')
            else:
                break
        else:
            print('NISN harus berupa angka!')
    data_siswa.append({'nama':nama_siswa, 'nisn':nisn_siswa})
    print('Nama telah ditambahkan')

def tampil():
    index = 1
    if len(data_siswa) <= 0:
        print('Data masih kosong!')
    else:
        data_siswa.sort(key=lambda y:y['nama'])
        for siswa in data_siswa:
            print(f"{index}. {siswa['nama']} {siswa['nisn']}")
            index+=1

def cari():
    while True:
        data_nisn = (input('Masukkan NISN siswa yang di cari: '))
        if len(data_nisn) <= 8 and data_nisn.isdigit():
            break
        else:
            print('NISN harus berupa angka!')
    for siswa in data_siswa:
        if data_nisn == siswa['nisn']:
            print('Nama di temukan')
            print('Nama: ' + siswa['nama'] + ' ' + siswa['nisn'])
            return
        print("Nama tidak di temukan")

def ubah():
    tampil()
    index = int(input('Pilih nomor dari nama siswa yang ingin di ganti: '))- 1
    nama_baru = input('Masukkan nama yang baru: ').capitalize()
    if any(siswa['nama'] == nama_baru for siswa in data_siswa):
        input('Nama sudah ada, apakah anda tetap ingin mengganti nama? (y/n):')
        if input == 'n':
            return
    while True:
        nisn_baru = (input('Masukkan NISN yang baru: '))
        if nisn_baru.isdigit() and len(nisn_baru) <= 8:
            if any(siswa['nisn'] == nisn_baru for siswa in data_siswa):
                print('NISN sudah ada')
            else:
                break
        else:
            print('NISN harus berupa angka')
    data_siswa[index] ['nama'] = nama_baru
    data_siswa[index] ['nisn'] = nisn_baru
    print('Data telah di ubah')

def hapus():
    tampil()
    index = int(input('Masukkan nomor dari nama siswa yang ingin di hapus: ')) - 1
    nama_hapus = data_siswa[index]['nama']
    del data_siswa[index]
    print(f'Nama siswa {nama_hapus} telah di hapus')


def menu():
    print('''
     ''')
    print('Pilih Menu yang di inginkan')
    print('1. Tambahkan Data Siswa')
    print('2. Tampilkan Semua Data Siswa')
    print('3. Cari Data Siswa Dari NISN')
    print('4. Ubah Data Siswa')
    print('5. Hapus Data Siswa')
    print('6. Keluar')

    pilihan = input('Pilih menu: ')
    if pilihan == '1':
        tambah()
    elif pilihan == '2':
        tampil()
    elif pilihan == '3':
        cari()
    elif pilihan == '4':
        ubah()
    elif pilihan == '5':
        hapus()
    elif pilihan == '6':
        sys.exit()
    else:
        print('Maaf tidak bisa')

while (True):
    menu()
