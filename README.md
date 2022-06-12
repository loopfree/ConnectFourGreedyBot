# Connect Four Bot Competition
made by Jonathan Christhoper Jahja\

### Changelog:
1. Added link to sheets

## Latar Belakang
Masih ingatkah kalian dengan tugas besar 1 stima kalian ? Kalian diminta membuat bot untuk memenangkan sebuah game balapan. Tujuan dari task ini adalah sama, yaitu membuat bot dengan menggunakan algoritma greedy. Tapi pada kali ini game yang berusaha dimenangkan adalah game Connect Four yang seharusnya tidak asing lagi didengar. Berbeda dengan task lainnya, task ini akan membandingkan hasil kerja kalian dengan teman seleksi lainnya dalam sebuah kompetisi. Jadi distribusi skor akan berdasarkan pemenang dari kompetisi. Maka kalian harus bisa membuat bot seoptimal mungkin. Good Luck Have Fun!

## Spesifikasi
* Pada task ini kalian akan membuat sebuah Bot Connect Four memanfaatkan algoritma Greedy
* Algoritma Greedy diimplementasikan pada folder `algorithm/`
* Pastikan algoritma yang diimplementasikan didalam sebuah class bernama `Bot<NIM kalian>` (contoh: `Bot13519144`) dan nama file `bot<NIM kalian>.py` (contoh: `bot13519144.py`)
* Berikut spesifikasi dari game Connect Four yang akan digunakan:
  1. Ukurang board adalah 6x7
  2. Thinking time dari bot maksimal 3 detik
* **Dilarang** mengambil atau menggunakan algoritma dari internet ataupun teman seleksi lainnya. 
* **Dilarang** mengimplementasikan algoritma selain metode Greedy
* Peserta yang melanggar aturan diatas akan diskualifikasi dari kompetisi dan tidak dapat mendapatkan skor.

## Teknis Kompetisi
* Kompetisi dimulai ketika submisi pertama dilakukan
* Kompetisi ini akan berlangsung selama keberjalanan seleksi asisten IRK
* Pemenang dari kompetisi akan ditentukan dari peserta yang berhasil mengumpulkan poin terbanyak di akhir kompetisi (**berbeda dengan poin seleksi**)
* Peserta dapat mengumpulkan poin dengan menjadi **King** dari memenangkan **daily tournament** yang akan diadakan setiap harinya pada siang hari (sekitar 12.00 - 15.00 WIB)
* Berikut adalah contoh bentuk bracket dari **Daily tournament**,
![](https://github.com/jonathan-cj/ConnectFourGame/blob/main/images/bracket.png)
> pada contoh dapat dilihat `Bot D` adalah pemenang dari **Daily tournament** tersebut, sehingga dia berhasil menjadi **King** dan mendapatkan poin.
* Prioritas urutan bracket dimulai dari bot yang masih menjadi **King**, dan diikuti oleh bot peserta yang mengumpulkan tercepat. 
> jadi pada contoh diatas `Bot A` merupakan **King** sebelumnya sehingga dia langsung ditempatkan di urutan pertama atau final. Lalu karena urutan pengumpulan Bot adalah `Bot B` > `Bot C` > `Bot D`, maka `Bot B` akan ditempatkan di urutan kedua, `Bot C` akan ditempatkan di urutan ketiga, dan seterusnya.
* Peserta yang berhasil menjadi **King** mendapatkan mulai dari 2 poin yang akan bertambah seiring keberjalanan kompetisi
* Jika seri maka pemenang ditentukan dari waktu submisi bot tercepat
* Scoreboard kompetisi dan informasi **Daily tournament** dapat dilihat pada [sheet berikut](https://docs.google.com/spreadsheets/d/1514xQfherR1aWXIZUiCZsn_1PPJT4MK60wK0K36w0i8/edit?usp=sharing)
* Berikut distribusi skor pada pemenang kompetisi:

| Posisi | Poin Seleksi |
| ----------- | ----------- |
| 1   | 2500 |
| 2   | 2250 |
| 3   | 2000 |
| 4   | 1750 |
| 5   | 1500 |
| 6 | 1250 |
| 7 | 1000 |
| 8 | 750 |
| 9 - dst. | 500 |

## Pengerjaan & Pengumpulan Bot
1. Clone repository ini pada sebuah repository private pada github Anda dan invite `jonathan-cj` ke dalam repository tersebut.
2. Cara menjalankan game/program terdapat di file [game-readme.md](game-readme.md)
3. Hubungi Line `jonathanjahja` untuk melakukan submisi bot.
4. Memberikan tag `vn` pada commit terakhir Anda setiap kali ingin melakukan submisi bot dengan n adalah urutan submisi keberapa. (contoh: `v1` untuk submisi pertama)
5. Setiap peserta maksimal hanya dapat melakukan submisi bot sebanyak 5x, jadi pastikan bot yang dikumpulkan tidak ada error atau bug.
6. Jika ada pertanyaan silahkan buat issues di [repository original](https://github.com/jonathan-cj/ConnectFourGame)

## Credit
Thanks to tugas besar AI buat inspirasinya
