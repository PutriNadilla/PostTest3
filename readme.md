Nama : Putri Nadilla Maharani
NIM : 2209116084
Kelas : Sistem Informasi B 2022

## Cara Kerja Program
Ketika awal program dijalankan, user akan diminta untuk memilih menu yang telah tersedia. Jika user memilih pilihan menu yang pertama maka user akan diminta untuk menambahkan judul film, genre, dan rating film yang ingin di tambahkan kedalam playlist, dan akan otomatis tersimpan di dalam playlist. Jika user memilih pilihan menu yang kedua maka user akan diminta untuk mengetikkan judul film yang ingin dihapus, jika sudah terhapus maka akan ditampilkan bahwa film telah terhapus dari playlist. Jika user memilih pilihan menu yang ketiga maka akan ditampilkan film-film yang terdapat pada playlist, bila user belum ada menambahkan film, maka program akan menampilkan bahwa playlist masih kosong atau belum ada data. Jika user memilih pilihan menu yang keempat maka program akan terhenti. Dan apabila user memasukkan inputan yang tidak sesuai dengan yang telah tersedia maka akan ditampilkan bahwa pilihan yang dimasukkan invalid maka akan disuruh untuk memilih kembali.

## Fungsionalitas
Linked List pada program ini digunakan untuk mengimplementasikan struktur data seperti array yang berupa sekumpulan node (simpul) yang saling terhubung secara linear dengan node lain melalui sebuah pointer. Node-node tersebut tidak disimpan secara berdampingan seperti array, tetapi terpencar-pencar di dalam memory sehingga dibutuhkan pointer yang menghubungkan satu node ke node berikutnya. 

## Sistem Kerja Aplikasi
Sistem kerja pada aplikasi ini adalah untuk menambahkan film, menghapus film, dan melihat display playlist yang dimana program tersebut saling terhubung satu dengan yang lainnya. Pada saat ingin menambahkan film, maka otomatis akan langsung tertambah kedalam display playlist. Kemudian jika ingin menghapus sebuah film pada display playlist, film tersebut akan otomatis terhapus dengan mengetikkan judul film yang ingin dihapus.

## Output program
Setelah program dijalankan akan ditampilkan output yaitu daftar menu yang tersedia, kemudian pengguna akan diminta memasukkan pilihan menu yang ingin dijalankan. Jika user memilih pilihan 1 maka output yang akan ditampilkan adalah data yang telah ditambahkan oleh user. Jika user memilih pilihan 2 maka output yang akan ditampilkan adalah data yang telah di hapus oleh user. Jika user memilih pilihan 3 maka output yang akan ditampilkan adalah data playlist yang telah ditambah maupun di hapus oleh user. Kemudian yang terakhir jika user memilih pilihan 4 maka output yang akan ditampilkan adalah proses pemberhentian program.

## Elemen Penting
class Movie:
    def __init__(self, title, genre, rating):

     def __str__(self):
        return f"{self.title} - {self.genre} ({self.rating})"

class Node:
    def __init__(self, movie):
        self.movie = movie
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None

def add_movie(self, movie):
        new_node = Node(movie)

def remove_movie(self, movie_title):
    current_node = self.head
    previous_node = None

def display_playlist(self):
        current_node = self.head

my_playlist = Playlist()

Class digunakan untuk menghubungkan setiap node sekaligus menyimpan data dan pointer ke node berikutnya.
def str difungsikan untuk merepresentasi string pada objek.
def init digunakan untuk menginisialisasi atribut suatu objek.
add digunakan untuk menambahkan data.
remove dugunakan untuk menghapus data. 
head node digunakan untuk menunjukkkan awal dari linked list.