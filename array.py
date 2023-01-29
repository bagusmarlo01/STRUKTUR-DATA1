dari   array   impor   array

def   kuadrat ( angka ):
    mengembalikan   nomor   *   nomor

# Menjawab Soal No 1
mahasiswa   = {
    "nim" : "20121067",
    "nama" : "Bagus Prastyo" ,
    "kelas" : "TI 3B" ,
    "alamat" : "Dukuh karangsari, karangasem utara, Batang"
}

# Menjawab Soal No 2
cetak ( "-------------------------------------------------- --- --------------" )
print ( "Aplikasi sederhana menggunakan String dan Array" )
cetak ( "-------------------------------------------------- --- --------------" )
print ( "NIM : {}" .format ( mahasiswa [ ' nim ' ] ) )
print ( "Nama : {}" .format ( mahasiswa [ ' nama ' ] ) )
print ( "Kelas : {}" .format ( mahasiswa [ ' kelas ' ] ) )
print ( "Alamat : {}" . format ( mahasiswa [ 'alamat' ] ) )
cetak ( "-------------------------------------------------- --- --------------" )
cetak ()

# Menjawab Soal No 3
urutkankata   = ( "UNISS" , "di" , "belajar" , "pada" , "Mahasiswa" , "data" , "ruang" , "lab" , "struktur" , "semester" , "tema" , "Array" , "Rangkai" , "dan" , "di" , "dengan" , "Batang" , 3 )
cetak ( "{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}" . format (
    urutkankata [ 4 ],
    urutkankata [ 1 ],
    urutkankata [ 0 ],
    urutkankata [ 16 ],
    urutkankata [ 3 ],
    urutkankata [ 9 ],
    urutkankata [ 17 ],
    urutkankata [ 2 ],
    urutkankata [ 8 ],
    urutkankata [ 5 ],
    urutkankata [ 15 ],
    urutkankata [ 10 ],
    urutkankata [ 12 ],
    urutkankata [ 13 ],
    urutkankata [ 11 ],
    urutkankata [ 14 ],
    urutkankata [ 6 ],
    urutkankata [ 7 ]
))
cetak ()


# Menjawab Soal No 4
nilai   =   array ( "i" , [ 1 , 3 , 4 , 5 , 10 , 15 , 20 ])
cetak ( "-------------------------------------------------- ----------------" )
print ( "Aplikasi sederhana menggunakan Array" )
cetak ( "-------------------------------------------------- ----------------" )
a   =   nilai [ 4 ] +   nilai [ 1 ] *   nilai [ 5 ]
b   =   nilai [ 1 ] *   nilai [ 2 ] /   2
c   =   kuadrat ( nilai [ 5 ]) *   nilai [ 1 ] +   nilai [ 3 ]
d   =   nilai [ 5 ] -   nilai [ 3 ] *   nilai [ 2 ]
print ( "a.{} + {} x {} = {}" . format ( nilai [ 4 ] , nilai [ 1 ] , nilai [ 5 ], a ))
print ( "b.{} x {} : 2 = {}" . format ( nilai [ 1 ], nilai [ 2 ] , int ( b )))
print ( "c.{}² x {} + {} = {}" . format ( nilai [ 5 ] , nilai [ 1 ] , nilai [ 3 ], c ))
print ( "d.{} - {} x {} = {}" .format ( nilai [ 5 ] , nilai [ 3 ] , nilai [ 2 ], d ))
cetak ()

# Selesai
