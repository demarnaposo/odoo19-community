# Odoo 19 Community Monorepo

Repository ini berisi environment development Odoo 19 Community dengan kumpulan addon custom, addon OCA, dan addon vendor dalam satu workspace.

## Ringkasan

- Platform: Odoo 19 Community
- Database: PostgreSQL 16
- Struktur: monorepo
- Fokus pengembangan: folder custom_addons

## Struktur Repository

- odoo/: source code core Odoo
- custom_addons/: addon custom, OCA, dan vendor
- odoo.conf: konfigurasi Odoo lokal
- data/: data runtime lokal (filestore, sessions, dll.)
- postgres/: data directory PostgreSQL lokal
- AGENTS.md: panduan kerja agent coding untuk repo ini

## Requirement Minimum

- Python 3.10+ (disarankan sesuai kompatibilitas Odoo 19)
- PostgreSQL 16
- pip dan virtual environment (disarankan)

## Setup Cepat

1) Masuk ke folder core Odoo

```bash
cd /Users/waldemarnaposo/project/odoo19/odoo
```

2) Install dependency Python

```bash
python3 -m pip install -r requirements.txt
```

3) Jalankan Odoo dengan addons path lokal eksplisit

```bash
python3 odoo-bin \
  -c ../odoo.conf \
  -d <db_name> \
  --addons-path=addons,odoo/addons,../custom_addons
```

Catatan:
- Meskipun odoo.conf sudah punya addons_path, untuk pengembangan lokal tetap disarankan override dengan flag --addons-path seperti di atas.

## Workflow Harian

Install modul:

```bash
python3 odoo-bin \
  -c ../odoo.conf \
  -d <db_name> \
  --addons-path=addons,odoo/addons,../custom_addons \
  -i <module_name>
```

Upgrade modul:

```bash
python3 odoo-bin \
  -c ../odoo.conf \
  -d <db_name> \
  --addons-path=addons,odoo/addons,../custom_addons \
  -u <module_name>
```

Jalankan test per modul:

```bash
python3 odoo-bin \
  -c ../odoo.conf \
  -d <db_name> \
  --addons-path=addons,odoo/addons,../custom_addons \
  --test-enable \
  --test-tags /<module_name> \
  --stop-after-init
```

Masuk Odoo shell:

```bash
python3 odoo-bin \
  -c ../odoo.conf \
  -d <db_name> \
  --addons-path=addons,odoo/addons,../custom_addons \
  shell
```

## Konvensi Pengembangan

- Utamakan patch kecil dan terfokus.
- Jangan ubah modul yang tidak diminta.
- Pertahankan lisensi modul (AGPL/LGPL/OPL) dan hindari mixing kode lintas lisensi yang berisiko.
- Untuk modul OCA, hindari edit file generated kecuali memang diminta.

Detail aturan kerja agent ada di AGENTS.md.

## Cakupan Edisi

Repository ini ditujukan untuk Odoo 19 Community.
Jika solusi membutuhkan fitur Enterprise, harus ada konfirmasi eksplisit dan dependensi yang sesuai.

## Catatan PostgreSQL 16

Semua perubahan SQL, migration, index, dan constraint harus kompatibel dengan PostgreSQL 16.
Jika menyentuh SQL mentah atau migrasi schema/data, lakukan validasi dampak performa dasar dan kompatibilitas sintaks.

## Troubleshooting Singkat

- Module tidak kebaca:
  - pastikan --addons-path sudah memuat ../custom_addons
- Error saat upgrade:
  - cek manifest module (depends, data/assets path)
- Test gagal:
  - jalankan ulang dengan test-tags per modul agar akar masalah lebih cepat terisolasi

## Kontribusi

- Lakukan perubahan per modul, kecil, dan bisa direview.
- Jalankan minimal upgrade modul + test modul terkait sebelum merge.
- Sertakan ringkasan dampak dan risiko sisa saat handoff/PR.

## Lisensi

Repo ini berisi modul dengan lisensi campuran (contoh AGPL-3, LGPL-3, OPL-1).
Selalu cek lisensi masing-masing modul di file __manifest__.py sebelum melakukan reuse kode.
