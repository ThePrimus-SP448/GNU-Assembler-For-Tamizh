#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "========================================================="
echo "  STARTING CLASSICAL TAMIZH GNU ASSEMBLER BUILD ENGINE  "
echo "========================================================="

# Get the exact absolute directory path of where this script lives
SRC_DIR="$(pwd)/binutils-gdb"

# 1. Navigate to the cloned repository directory safely using quotes
cd "$SRC_DIR"

# 2. Check if Makefile already exists; if not, configure the workspace
if [ ! -f Makefile ]; then
    echo "--> Configuring workspace for x86_64 target architecture..."
    ./configure --target=x86_64-linux-gnu --disable-werror
fi

echo "--> Compiling the modified GNU Assembler (gas)..."
# 3. Compile gas and opcodes with explicit space safety
make all-gas all-opcodes -j$(nproc)

echo "========================================================="
echo "          BUILD SUCCESSFUL! EXECUTABLE READY            "
echo "  Location: binutils-gdb/gas/as-new                     "
echo "========================================================="
