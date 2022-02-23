data_peminjam = [{
        'Kode Buku' : '11A',
        'Nama' : 'Rudi Waluyo',
        'Kelas' : '11',
        'Judul' : 'Dampak Rumah Kaca', 
        'Penerbit' : 'CV. Pamularsih'
    },
    {
        'Kode Buku' : '11B',
        'Nama' : 'Firly Putri',
        'Kelas' : '11',
        'Judul' : 'Flora Lima Benua', 
        'Penerbit' : 'CV. Ghiyas Putra'
    },
    {
        'Kode Buku' : '11C', 
        'Nama' : 'Kevin Salim',
        'Kelas' : '10',
        'Judul' : 'Mengenal Laut Indonesia', 
        'Penerbit' : 'CV. Sinar Cemerlang Abadi'
    }]

# Read Data
def read_data():
    read = True
    while read != '3':
        print('''
+++++++ Laporan Data Peminjam Buku +++++++
1. Laporan seluruh data
2. Laporan data tertentu
3. Kembali Ke Menu Utama''')
        read = input('Silahkan Pilih Sub Menu Read Data [1-3] : ')
        if read == '1':
            if len(data_peminjam) != 0:
                print('Daftar Buku :')
                for j, i in enumerate(data_peminjam):
                    print(f"{j+1}. Kode Buku : {i['Kode Buku']}, Nama : {i['Nama']}, Kelas : {i['Kelas']}, Judul : {i['Judul']}, Penerbit : {i['Penerbit']}")
            else:
                print('\n++++ Tidak Terdapat Data Siswa ++++')
            continue
        elif read == '2':
            if len(data_peminjam) != 0:
                kode = input('Masukkan Kode Buku : ')
                print(f'Data Buku dengan Kode : {kode}')
                for j, i in enumerate(data_peminjam):
                    if i['Kode Buku'] == kode:
                        print(f"{j+1}. Kode Buku : {i['Kode Buku']}, Nama : {i['Nama']}, Kelas : {i['Kelas']}, Judul : {i['Judul']}, Penerbit : {i['Penerbit']}")
                        break
                else:
                    print('\n++++ Tidak Terdapat Kode tersebut ++++')
                    break
            else:
                print('\n++++ Tidak Terdapat Data Siswa ++++')
                break
        elif read == '3':
            break
        else:
            print('\nPilihan Sub Menu Tidak Terdaftar')
    return

# Create Data
def create_data():
    create = True
    while create != '2':
        print('''
+++++++ Tambah Data Peminjaman Buku +++++++
1. Tambah data siswa
2. Kembali ke Menu Utama''')
        create = input('Silahkan Pilih Sub Menu Tambah Data [1-2] : ')
        if create == '1':
            kode = input('Masukkan Kode Buku : ')
            for j, i in enumerate(data_peminjam):
                if len(data_peminjam) != 0:
                    if i['Kode Buku'] == kode:
                        print('Data Sudah Ada')
                        break       
            else:
                nama = input('Masukkan Nama : ')
                kelas = input('Masukkan Kelas : ')
                judul = input('Masukkan Judul : ')
                penerbit = input('Masukkan Penerbit : ')
                while True:
                    simpanCreate = input('Apakah Data akan disimpan? (Yes/No) : ')
                    if simpanCreate == 'Yes' or simpanCreate == 'yes':
                        data_peminjam.append({'Kode Buku' : kode,  'Nama' : nama, 'Kelas' : kelas, 'Judul' : judul, 'Penerbit' : penerbit})
                        print('Data Berhasil Disimpan')
                        break
                    elif simpanCreate == 'No' or simpanCreate == 'no':
                        print('Data Tidak Disimpan')
                        break
                    else:
                        continue
            break
        elif create == '2':
            break
        else:
            print('\nPilihan Sub Menu Tidak Terdaftar')
    return

# Update Data
def update_data():
    update = True
    while update != '2':
        print('''
+++++++ Ubah Data Peminjaman Buku  +++++++
1. Ubah data siswa
2. Kembali ke Menu Utama''')
        update = input('Silahkan Pilih Sub Menu Ubah Data [1-2] : ')
        if update == '1':
            kode = input('Masukkan Kode Buku : ' )
            for j, i in enumerate(data_peminjam):
                if i['Kode Buku'] == kode:
                    print(f"{j+1}. Kode Buku : {i['Kode Buku']}, Nama : {i['Nama']}, Kelas : {i['Kelas']}, Judul : {i['Judul']}, Penerbit : {i['Penerbit']}")
                    while True:
                        simpanKode = input('Apakah data akan dilanjutkan melakukan update? (Yes/No) : ')
                        if simpanKode == 'Yes' or simpanKode == 'yes':
                            while True:
                                gantiKode = input('Masukkan kolom yang ingin diedit : ')
                                if gantiKode == 'nama' or gantiKode == 'Nama':
                                    namaBaru = input('Masukkan nama baru : ')
                                    while True:
                                        tanya = input('Apakah data akan diupdate? (Yes/No) : ')
                                        if tanya == "Yes" or tanya == 'yes':
                                            data_peminjam[j]["Nama"] = namaBaru
                                            print("\nData berhasil di update")
                                            break
                                        elif tanya == 'No' or tanya == 'no':
                                            print('\nData tidak diupdate')
                                            break
                                        else:
                                            continue
                                    break
                                elif gantiKode == 'kelas' or gantiKode == 'Kelas':
                                    kelasBaru = input('Masukkan kelas Baru : ')
                                    while True:
                                        tanya = input('Apakah data akan diupdate? (Yes/No) : ')
                                        if tanya == "Yes" or tanya == 'yes':
                                            data_peminjam[j]["Kelas"] = kelasBaru
                                            print("Data berhasil di update")
                                            break
                                        elif tanya == 'No' or tanya == 'no':
                                            print('Data tidak diupdate')
                                            break
                                        else:
                                            continue
                                    break
                                elif gantiKode == 'judul' or gantiKode == 'Judul':
                                    judulBaru = input('Masukkan judul Baru : ')
                                    while True:
                                        tanya = input('Apakah data akan diupdate? (Yes/No) : ')
                                        if tanya == "Yes" or tanya == 'yes':
                                            data_peminjam[j]["Judul"] = judulBaru
                                            print("Data berhasil di update")
                                            break
                                        elif tanya == 'No' or tanya == 'no':
                                            print('Data tidak diupdate')
                                            break
                                        else:
                                            continue
                                    break
                                elif gantiKode == 'penerbit' or gantiKode == 'Penerbit':
                                    penerbitBaru = input('Masukkan penerbit baru : ')
                                    while True:
                                        tanya = input('Apakah data akan diupdate? (Yes/No) : ')
                                        if tanya == "Yes" or tanya == 'yes':
                                            data_peminjam[j]["Penerbit"] = penerbitBaru
                                            print("Data berhasil diupdate")
                                            break
                                        elif tanya == 'No' or tanya == 'no':
                                            print('Data tidak diupdate')
                                            break
                                        else:
                                            continue       
                                    break
                                else:
                                    print('\n++++ Tidak Ada Kolom tersebut pada data Perpustakaan ++++\n')
                                    break
                            break
                        elif simpanKode == 'No' or simpanKode == 'no':
                            print('\nData Tidak Jadi Diupdate')    
                            break
                        else:
                            continue
                    break        
            else:
                print('\n+++++ Data Tidak Ada +++++')
                continue
        elif update == '2':
            break
        else:
            print('\nPilihan Sub Menu Tidak Terdaftar')
    return

# Delete Data
def delete_data():
    delete = True
    while delete != '2':
        print('''
+++++++ Hapus Data Peminjaman Buku +++++++
1. Hapus data siswa
2. Kembali ke Menu Utama''')
        delete = input('Silahkan Pilih Sub Menu Hapus Data [1-2] : ')
        if delete == '1':
            inputDel = input('Masukkan kode buku : ')
            for j, i in enumerate(data_peminjam):
                if i['Kode Buku'] == inputDel:
                    print(f"{j+1}. Kode Buku : {i['Kode Buku']}, Nama : {i['Nama']}, Kelas : {i['Kelas']}, Judul : {i['Judul']}, Penerbit : {i['Penerbit']}")
                    while True:
                        tanya = input('Apakah Data akan Dihapus? (Yes/No) : ')
                        if tanya == 'Yes' or tanya == 'yes':
                            data_peminjam[j]['Kode Buku'] == inputDel
                            del data_peminjam[j]
                            print('\nData berhasil dihapus')
                            break
                        elif tanya == 'No' or tanya == 'no':
                            print('\nData tidak dihapus')
                            break
                        else:
                            continue
                    break
            else:
                print('Data Tidak Ada')
                continue
        elif delete == '2':
            break
        else:
            print('\nPilihan Sub Menu Tidak Terdaftar')
    return

while True:
    Menu = input('''
++++ Selamat Datang di Perpustakaan SMA Suka Maju ++++

Berikut daftar menu data peminjaman buku : 
1. Laporan Data Peminjaman Buku
2. Tambah Data Peminjaman Buku
3. Ubah Data Peminjaman Buku
4. Hapus Data Peminjaman Buku
5. Keluar

Masukkan angka menu yang ingin dijalankan : ''')

    if (Menu == '1'):
        read_data()
    elif (Menu == '2'):
        create_data()
    elif (Menu == '3'):
        update_data()
    elif (Menu == '4'):
        delete_data()
    elif (Menu == '5'):
        print('\n++++ Thank you and Good Bye!!! ++++\n')
        break
    else:
        print('\n++++ Pilihan yang anda masukkan SALAH ++++\n')
        continue
