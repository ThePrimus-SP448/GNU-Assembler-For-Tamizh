import subprocess

# 1. Create a Tamizh assembly file using the custom mov mnemonic
# mov: \x94\x8d\x98\x9f
tamizh_asm = b'\x94\x8d\x98\x9f %rax, %rbx\n'

with open('test_tamizh.s', 'wb') as f:
    f.write(tamizh_asm)

print("Created test_tamizh.s with raw Tamizh mnemonic bytes.")

# 2. Run the newly built assembler
try:
    result = subprocess.run(
        ['binutils-gdb/gas/as-new', 'test_tamizh.s', '-o', 'test_tamizh.o'],
        capture_output=True,
        text=True,
        check=True
    )
    print("Assembler succeeded!")
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)
except subprocess.CalledProcessError as e:
    print("Assembler failed with exit code:", e.returncode)
    print("STDOUT:", e.stdout)
    print("STDERR:", e.stderr)
    exit(1)

# 3. Disassemble the output to verify it matches 'mov %rax, %rbx'
try:
    disasm = subprocess.run(
        ['objdump', '-d', 'test_tamizh.o'],
        capture_output=True,
        text=True,
        check=True
    )
    print("\nDisassembly of generated test_tamizh.o:")
    print(disasm.stdout)
except Exception as e:
    print("Disassembly failed:", e)
