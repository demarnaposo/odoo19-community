# AGENTS.md

## Tujuan
Dokumen ini mendefinisikan cara kerja agent coding di workspace odoo19 agar perubahan aman, terukur, bisa direview, dan konsisten dengan praktik Odoo/OCA.

## Ringkasan Audit (2026-08-04)
- Target platform: Odoo 19 Community (bukan Enterprise).
- Database engine: PostgreSQL 16.
- Struktur repo berbentuk monorepo:
  - Core Odoo di odoo/
  - Addon custom dan pihak ketiga di custom_addons/
  - Data PostgreSQL lokal di postgres/
  - Data runtime di data/
- Ekosistem addon campuran:
  - Addon gaya OCA (AGPL/LGPL, readme generated, tests tersedia)
  - Addon vendor/komersial (misal OPL-1)
  - Addon in-house
- Banyak modul punya tests, tetapi tidak ada satu script runner test global di root.
- odoo.conf ada di root, tetapi addons_path mengarah ke jalur paket/container. Untuk development lokal WAJIB override --addons-path saat menjalankan odoo-bin.

## Peta Repo
- Framework backend utama: odoo/
- Scope default pengembangan: custom_addons/
- Edisi target: Odoo 19 Community.
- Struktur modul yang umum:
  - __manifest__.py
  - models/, views/, security/, wizard/, data/
  - opsional: tests/, static/, demo/, readme/

## Batasan Edisi (Community)
- Semua solusi WAJIB kompatibel dengan Odoo 19 Community.
- DILARANG mengandalkan fitur/modul Enterprise kecuali user eksplisit meminta dan menyediakan dependensinya.
- Jika usulan perubahan butuh modul Enterprise, agent WAJIB:
  - berhenti dan minta konfirmasi user
  - jelaskan dependency Enterprise yang dibutuhkan
  - tawarkan alternatif implementasi Community jika memungkinkan

## Batasan Database (PostgreSQL 16)
- Semua perubahan query SQL, index, constraint, dan migration WAJIB kompatibel dengan PostgreSQL 16.
- DILARANG mengandalkan perilaku lama PostgreSQL yang sudah berubah/deprecated di v16.
- Jika perubahan menyentuh SQL mentah atau migrasi schema/data, agent WAJIB:
  - validasi dampak performa dasar (misal query plan/index yang relevan)
  - memastikan tidak ada syntax/fitur yang tidak kompatibel dengan PostgreSQL 16

## Aturan Kerja Agent (Strict)
Semua aturan di bawah bersifat WAJIB kecuali user memberi instruksi yang jelas untuk override.

### 1) Scope dan Dampak
- WAJIB membuat patch sekecil mungkin.
- DILARANG mengubah modul yang tidak diminta.
- Default scope adalah custom_addons/. Edit ke odoo/ hanya jika user eksplisit meminta.
- DILARANG melakukan refactor besar lintas modul dalam satu task tanpa persetujuan user.

### 2) Lisensi dan Provenance
- WAJIB mempertahankan lisensi di manifest dan header file.
- DILARANG menyalin kode dari modul OPL ke modul AGPL/LGPL jika berpotensi melanggar kompatibilitas lisensi.
- Untuk modul OCA, WAJIB mengikuti pola OCA yang sudah ada.

### 3) File Generated
- DILARANG edit file generated kecuali user minta langsung:
  - README.rst generated (OCA)
  - static/description/index.html generated dari readme
- Jika perubahan fungsional butuh update dokumen generated, edit source readme-nya dan catat bahwa regenerasi diperlukan.

### 4) Data dan Operasi Berisiko
- DILARANG menjalankan operasi destruktif database tanpa izin user.
- DILARANG menghapus data migrasi, security, atau XML data file tanpa analisis dampak.
- WAJIB meminta konfirmasi sebelum rename model/field yang berpotensi breaking.

## Perintah Lokal (Wajib Pakai Addons Path Eksplisit)
Jalankan dari folder odoo/:

```bash
cd /Users/waldemarnaposo/project/odoo19/odoo
```

Jalankan server:

```bash
python3 odoo-bin \
  -c ../odoo.conf \
  -d <db_name> \
  --addons-path=addons,odoo/addons,../custom_addons
```

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

Test per modul (minimal gate):

```bash
python3 odoo-bin \
  -c ../odoo.conf \
  -d <db_name> \
  --addons-path=addons,odoo/addons,../custom_addons \
  --test-enable \
  --test-tags /<module_name> \
  --stop-after-init
```

Shell Odoo:

```bash
python3 odoo-bin \
  -c ../odoo.conf \
  -d <db_name> \
  --addons-path=addons,odoo/addons,../custom_addons \
  shell
```

## Quality Gate Wajib (Harus Lolos Sebelum Selesai)
Untuk setiap perubahan modul:
1. Validasi manifest:
   - depends sesuai perubahan
   - data/assets berisi file yang benar-benar ada
   - versi dinaikkan jika policy tim meminta
2. Jalankan upgrade modul yang disentuh.
3. Jalankan test tags minimal /<module_name>.
4. Cek regresi umum Odoo:
   - security/access (ir.model.access.csv, rule, group)
   - error XML/view loading
   - missing file di manifest
   - asset bundle web.assets_* rusak/path salah
5. Jika menyentuh alur accounting/payroll/subscription/helpdesk:
   - WAJIB uji satu skenario end-to-end realistis.

Jika salah satu gate gagal:
- Status task HARUS dianggap belum selesai.
- Agent WAJIB melaporkan error dan akar masalah singkat.

## Standar Implementasi
- Python:
  - Ikuti gaya Odoo dan pola modul sekitar.
  - Utamakan extend model existing dibanding duplikasi logic.
  - Hindari perubahan API publik tanpa alasan kuat.
- JS/OWL:
  - Ikuti struktur asset modul yang sudah ada.
  - Pastikan deklarasi assets di manifest sinkron dengan file aktual.
- Komentar:
  - Hanya untuk logic yang tidak obvious, singkat, dan relevan.

## Checklist Handoff (Wajib Dilaporkan)
Sebelum menutup task, agent WAJIB menyatakan:
- File apa saja yang diubah.
- Scope tetap sesuai request.
- Hasil upgrade/test (jalan/gagal, ringkasan singkat).
- Risiko sisa (jika ada) dan dampaknya.

## Kondisi Wajib Minta Konfirmasi User
Agent HARUS berhenti dan minta konfirmasi jika:
- Perlu refactor besar lintas modul.
- Perlu migrasi data/backfill yang signifikan.
- Perlu operasi destruktif DB atau penghapusan data penting.
- Menemukan perubahan tak terduga di file yang sama (kemungkinan konflik kerja paralel).

## Prinsip Eksekusi
- Prioritaskan perubahan incremental ukuran kecil.
- Jangan kompromi pada validasi minimum.
- Lebih baik kirim patch kecil yang lolos gate daripada patch besar yang berisiko.
