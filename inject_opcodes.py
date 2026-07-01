import re
import os

# Define absolute file paths
table_path = "binutils-gdb/opcodes/i386-opc.tbl"
backup_path = "binutils-gdb/opcodes/i386-opc.tbl.bak"

# 1. Back up the original file if it hasn't been done already
if not os.path.exists(backup_path):
    os.system(f"cp {table_path} {backup_path}")
    print(f"[*] Created original table backup at: {backup_path}")

# 2. Master Translation Dictionary (English Mnemonic -> Tamizh Hex Byte String)
# Hand-mapped using the optimized Uyirmei-baseline matrix with the 159-Pulli bridge slot
translation_map = {
    "mov": r"\x94\x8D\x98\x9F",
    "push": r"\x95\xA3\x8D\xA3",
    "pop": r"\x86\x91\xA3",
    "lea": r"\x82\x91\x96\x9F",
    "movzx": r"\x95\xA0\x94",
    "movsx": r"\x8D\xA3\x94",
    "xchg": r"\x96\xA0\x9D\xA3",
    "cmov": r"\x8F\xA0\x94",
    "add": r"\x8D\xA4",
    "sub": r"\x8D",
    "mul": r"\x95\xA5",
    "div": r"\x9A",
    "imul": r"\x8D\xA3\x95\xA5",
    "idiv": r"\x8D\xA3\x9A",
    "inc": r"\x96\xA1\x8D\xA3",
    "dec": r"\x8D\xA3\x9D\xA7",
    "neg": r"\x86\x93\xA1",
    "and": r"\x84\x96\x9F",
    "or": r"\x80\x99\x9F",
    "xor": r"\x9A\xA1\x99",
    "not": r"\x96\x9D\xA3",
    "cmp": r"\x89\x95\x9F",
    "test": r"\x81\x97\x9F",
    "shl": r"\x82\x94",
    "shr": r"\x9A\x94",
    "sal": r"\x86\x82\x94",
    "sar": r"\x86\x9A\x94",
    "rol": r"\x82\x8F\xA3",
    "ror": r"\x9A\x8F\xA3",
    "jmp": r"\x93\xA0",
    "je": r"\x8F\x95",
    "jz": r"\x95\xA0\x95",
    "jne": r"\x9A\xA6\x95",
    "jnz": r"\x94\xA1\x95",
    "jg": r"\x96\xA1\x95",
    "jge": r"\x96\xA1\x8F\x95",
    "jl": r"\x8D\xA3\x95",
    "jle": r"\x8D\xA3\x8F\x95",
    "call": r"\x80\x9B\xA7",
    "ret": r"\x96\xA2",
    "syscall": r"\x80\x80\x9B\xA7",
    "int": r"\x96\x9D\xA1",
    "nop": r"\x9A\x9D\xA1",
    "clc": r"\x93\xA3\x91\xA7",
    "stc": r"\x94\xA1\x9D\xA3\x9A\xA3"
}

print("[*] Beginning injection of classical Tamizh mnemonics...")

new_lines = []
injected_count = 0

with open(backup_path, "r") as f:
    for line in f:
        # Keep the original instruction layout intact
        new_lines.append(line)
        
        # Check if the line matches an instruction pattern: starts with alphanumeric characters followed by a comma
        match = re.match(r"^([a-z0-9]+),", line)
        if match:
            eng_mnemonic = match.group(1)
            
            # If the mnemonic exists in the translation map, clone the entry using the new Tamizh hex token
            if eng_mnemonic in translation_map:
                tamizh_hex = translation_map[eng_mnemonic]
                # Safely replace only the initial prefix mnemonic string definition
                tamizh_line = line.replace(f"{eng_mnemonic},", f"{tamizh_hex},", 1)
                new_lines.append(tamizh_line)
                injected_count += 1

# 3. Save the mutated instruction tree back into the master table file
with open(table_path, "w") as f:
    f.writelines(new_lines)

print(f"[+] Success! Programmatically injected {injected_count} Tamizh short-form variations into the opcode mapping layout.")
