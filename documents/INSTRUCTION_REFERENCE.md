# தமிழ் GNU AS (Tamil GNU Assembler) — Instruction Reference
**A Pure Classical Tamizh (Senthamizh) Mnemonic Specification for x86-64**  
*Target Integration: `binutils-gdb/opcodes/i386-opc.tbl`*  
*Author: Surendhiran | Version: 1.1 — Production Final*

---

## 1. Overview & Architectural Principles

1. **Pure Classical Senthamizh Only**: Zero Grantha characters, zero Sanskrit loanwords, and zero colloquial hybrid coinages[cite: 3].
2. **Action-Oriented Semantics**: Every mnemonic describes physical silicon execution rather than literal translation[cite: 3].
3. **8-Bit Extended ASCII Architecture**: Each Tamizh token (vowel, root consonant, pulli, vowel modifier, numeral) maps strictly to a single byte in the `128–255` range to eliminate UTF-8 multi-byte parsing loops[cite: 3].
4. **Collision-Free Ergonomics**: All 45 short-form mnemonics are fully collision-tested for fast typing in low-level systems programming[cite: 3].

---

## 2. Complete 45-Instruction Reference Table

| Category | Intel Mnemonic | Tamil Mnemonic | Short Form | 8-Bit Hex Byte String | Literal Meaning | Hardware Function |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Data Movement** | `mov` | நகர் | **நகர்** | `\x94\x8D\x98\x9F` | Move / Transfer | Copies data from source to destination operand[cite: 3]. |
| | `push` | புகு | **புகு** | `\x95\xA3\x8D\xA3` | Enter / Push in | Decrements RSP and pushes operand onto stack[cite: 3]. |
| | `pop` | எடு | **எடு** | `\x86\x91\xA3` | Take / Pick up | Pops top of stack into destination, increments RSP[cite: 3]. |
| | `lea` | இடம் | **இடம்** | `\x82\x91\x96\x9F` | Address / Location | Computes effective address and stores in destination[cite: 3]. |
| | `movzx` | பாழ்நகர் | **பாந** | `\x95\xA0\x94` | Zero-extend move | Copies smaller source to larger destination, zero-filling upper bits[cite: 3]. |
| | `movsx` | குறிநகர் | **குந** | `\x8D\xA3\x94` | Sign-extend move | Copies smaller source to larger destination, sign-filling upper bits[cite: 3]. |
| | `xchg` | மாறு | **மாறு** | `\x96\xA0\x9D\xA3` | Swap / Exchange | Exchanges contents of source and destination[cite: 3]. |
| | `cmov` | சார்நகர் | **சாந** | `\x8F\xA0\x94` | Conditional move | Moves operand only if condition flags are met[cite: 3]. |
| **Arithmetic** | `add` | கூட்டு | **கூ** | `\x8D\xA4` | Add / Accumulate | Adds source operand to destination operand[cite: 3]. |
| | `sub` | கழி | **க** | `\x8D` | Subtract / Reduce | Subtracts source operand from destination operand[cite: 3]. |
| | `mul` | பெருக்கு | **பெ** | `\x95\xA5` | Multiply | Performs unsigned multiplication: `RDX:RAX = RAX × src`[cite: 3]. |
| | `div` | வகு | **வ** | `\x9A` | Divide | Unsigned division: `RDX:RAX / src`; quotient $\rightarrow$ `RAX`[cite: 3]. |
| | `imul` | குறிபெருக்கு | **குபெ** | `\x8D\xA3\x95\xA5` | Signed multiply | Performs signed multiplication of two operands[cite: 3]. |
| | `idiv` | குறிவகு | **குவ** | `\x8D\xA3\x9A` | Signed divide | Signed division of `RDX:RAX` by divisor[cite: 3]. |
| | `inc` | மிகு | **மிகு** | `\x96\xA1\x8D\xA3` | Increase by one | Increments destination operand by 1[cite: 3]. |
| | `dec` | குறை | **குறை** | `\x8D\xA3\x9D\xA7` | Decrease by one | Decrements destination operand by 1[cite: 3]. |
| | `neg` | எதிர் | **எதி** | `\x86\x93\xA1` | Negate / Opposite | Two's complement negation of destination operand[cite: 3]. |
| **Logic** | `and` | உம் | **உம்** | `\x84\x96\x9F` | And / Conjunction | Performs bitwise logical AND[cite: 3]. |
| | `or` | அல் | **அல்** | `\x80\x99\x9F` | Or / Alternation | Performs bitwise logical OR[cite: 3]. |
| | `xor` | விலக்கல் | **வில** | `\x9A\xA1\x99` | Exclusive remove | Bitwise XOR — differing bits $\rightarrow$ 1, identical $\rightarrow$ 0[cite: 3]. |
| | `not` | மறு | **மறு** | `\x96\x9D\xA3` | Invert / Reverse | Inverts all bits (one's complement)[cite: 3]. |
| | `cmp` | ஒப்பி | **ஒப்** | `\x89\x95\x9F` | Compare | Subtracts without storing; updates EFLAGS[cite: 3]. |
| | `test` | ஆய் | **ஆய்** | `\x81\x97\x9F` | Examine / Test | Bitwise AND without storing; updates EFLAGS[cite: 3]. |
| **Shift / Rotate** | `shl` | இடநகர் | **இந** | `\x82\x94` | Shift left | Logical left shift; zero-fills right side[cite: 3]. |
| | `shr` | வலநகர் | **வந** | `\x9A\x94` | Shift right | Logical right shift; zero-fills left side[cite: 3]. |
| | `sal` | எண்இடநகர் | **எஇந** | `\x86\x82\x94` | Arithmetic left shift | Performs arithmetic left shift (identical to SHL)[cite: 3]. |
| | `sar` | எண்வலநகர் | **எவந** | `\x86\x9A\x94` | Arithmetic right shift | Arithmetic right shift; preserves sign bit[cite: 3]. |
| | `rol` | இடச்சுழல் | **இசு** | `\x82\x8F\xA3` | Rotate left | Circular left shift; high bits wrap to lowest[cite: 3]. |
| | `ror` | வலச்சுழல் | **வசு** | `\x9A\x8F\xA3` | Rotate right | Circular right shift; low bits wrap to highest[cite: 3]. |
| **Control Flow** | `jmp` | தாவு | **தா** | `\x93\xA0` | Leap / Jump | Unconditional transfer of execution control[cite: 3]. |
| | `je` | சமப்பாய் | **சப** | `\x8F\x95` | Jump if equal | Jumps if Zero Flag is set (`ZF=1`)[cite: 3]. |
| | `jne` | வேறுபாய் | **வேப** | `\x9A\xA6\x95` | Jump if not equal | Jumps if Zero Flag is clear (`ZF=0`)[cite: 3]. |
| | `jg` | மிகுபாய் | **மிப** | `\x96\xA1\x95` | Jump if greater | Signed comparison: jumps when `ZF=0` and `SF=OF`[cite: 3]. |
| | `jge` | மிகுசமப்பாய் | **மிசப** | `\x96\xA1\x8F\x95` | Jump if $\ge$ | Signed comparison: jumps when `SF=OF`[cite: 3]. |
| | `jl` | குறைபாய் | **குப** | `\x8D\xA3\x95` | Jump if less | Signed comparison: jumps when `SF≠OF`[cite: 3]. |
| | `jle` | குறைசமப்பாய் | **குசப** | `\x8D\xA3\x8F\x95` | Jump if $\le$ | Signed comparison: jumps when `ZF=1` or `SF≠OF`[cite: 3]. |
| | `jz` | பாழ்பாய் | **பாப** | `\x95\xA0\x95` | Jump if zero | Identical to `JE`; jumps when `ZF=1`[cite: 3]. |
| | `jnz` | நிறைபாய் | **நிப** | `\x94\xA1\x95` | Jump if not zero | Identical to `JNE`; jumps when `ZF=0`[cite: 3]. |
| | `call` | அழை | **அழை** | `\x80\x9B\xA7` | Call / Summon | Pushes next IP to stack, branches to function[cite: 3]. |
| | `ret` | மீள் | **மீ** | `\x96\xA2` | Return / Come back | Pops return address from stack and returns[cite: 3]. |
| **System / Misc** | `syscall` | அமைப்பழை | **அஅழை** | `\x80\x80\x9B\xA7` | System call | Invokes Linux kernel system call interface[cite: 3]. |
| | `int` | மறிவு | **மறி** | `\x96\x9D\xA1` | Interrupt / Halt flow | Triggers a software interrupt vector[cite: 3]. |
| | `nop` | வறிது | **வறி** | `\x9A\x9D\xA1` | Empty / Void action | No operation; consumes one CPU cycle[cite: 3]. |
| | `clc` | துடை | **துடை** | `\x93\xA3\x91\xA7` | Wipe / Clear | Clears Carry Flag (`CF = 0`)[cite: 3]. |
| | `stc` | நிறுவு | **நிறுவு** | `\x94\xA1\x9D\xA3\x9A\xA3` | Establish / Set | Sets Carry Flag (`CF = 1`)[cite: 3]. |