# தமிழ் GNU AS (Tamil GNU Assembler)
**A native pure classical Tamizh (Senthamizh) x86-64 assembler.**

Tamil GNU AS localizes GNU binutils' assembler (`gas`) to assemble machine code directly from pure classical Tamizh mnemonics and registers.

---

## Key Features

* **Pure Senthamizh Lexicon**: 45 action-based assembly mnemonics built strictly from classical roots (no Grantha, loanwords, or hybrid coinages).
* **Deterministic 8-Bit Encoding**: Custom Extended ASCII matrix (128–255) where 1 visible Tamizh character = 1 byte, bypassing multi-byte UTF-8 parsing bottlenecks.
* **Native ELF64 Output**: Produces standard Linux x86-64 object files linkable with standard `ld`.

---

## Quick Start

### 1. Build the Assembler
```bash
git clone [https://github.com/](https://github.com/)<your-username>/Tamizh_GNU_Assembler.git
cd Tamizh_GNU_Assembler
./build_gas.sh

```

### 2. Write Assembly (`test.s`)

```assembly
.global _start
.text
_start:
    நகர்  $60, %rax       # mov $60, %rax (sys_exit)
    நகர்  $0, %rdi        # mov $0, %rdi  (status code 0)
    அஅழை                  # syscall

```

### 3. Assemble and Link

```bash
./binutils-gdb/gas/as-new -o test.o test.s
ld -o test test.o
./test

```

---

## Documentation

Full specifications, character encoding tables, and contribution guidelines are in `/docs`:

* [`docs/INSTRUCTION_REFERENCE.md`](https://www.google.com/search?q=docs/INSTRUCTION_REFERENCE.md) — 45 core instruction mappings and hex byte strings.
* [`docs/ENCODING_SPECIFICATION.md`](https://www.google.com/search?q=docs/ENCODING_SPECIFICATION.md) — Custom 8-bit character layout and Pulli bridge details.
* [`docs/CONTRIBUTIONS.md`](https://www.google.com/search?q=docs/CONTRIBUTIONS.md) — Vocabulary guidelines and contribution standards.

---

## Author & License

* **Author**: Surendhiran
* **License**: GNU General Public License v3.0 (`GPL-3.0`)
