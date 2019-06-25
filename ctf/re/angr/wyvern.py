#!/usr/bin/env python
# coding: utf-8
import angr
import time

def main():
    # Load the binary. This is a 64-bit C++ binary, pretty heavily obfuscated.
    p = angr.Project('wyvern')

    # This block constructs the initial program state for analysis.
    # Because we're going to have to step deep into the C++ standard libraries
    # for this to work, we need to run everyone's initializers. The full_init_state
    # will do that. In order to do this peformantly, we will use the unicorn engine!
#    st = p.factory.full_init_state(args=['./wyvern'], add_options=angr.options.unicorn) #8m48
    st = p.factory.entry_state(add_options=angr.options.unicorn) #7m59
#    st = p.factory.entry_state() #14m37

    #A newline character makes fgets stop reading, but it is considered a valid character by the function and included in the string copied to str.
    #.text:00000000004046A7                 mov     r9d, legend (legend 73h)
    #.text:00000000004046AF                 sar     r9d, 2      (73h >> 2 = 28)
    #.text:00000000004046B6                 cmp     rax, rcx
    #.text:00000000004046B9                 setnz   r10b
    #.text:00000000004046FE                 mov     [rbp+var_41], r10b
    # It's reasonably easy to tell from looking at the program in IDA that the key will
    # be 29 bytes long, and the last byte is a newline.
# from pin_password.py: password length should be: [28]
    # Constrain the first 28 bytes to be non-null and non-newline:
    for _ in xrange(28):
        k = st.posix.files[0].read_from(1)
        st.solver.add(k >= 0x20, k <= 0x7e)

    # Constrain the last byte to be a newline
    k = st.posix.files[0].read_from(1)
    st.solver.add(k == 10)

    # Reset the symbolic stdin's properties and set its length.
    st.posix.files[0].seek(0)
    st.posix.files[0].length = 29

    # Construct a SimulationManager to perform symbolic execution.
    # Step until there is nothing left to be stepped.
    sm = p.factory.simulation_manager(st)
    sm.explore(find=0x40E070, avoid=[0x40E2AA, 0x40E36C])
    out = sm.one_found.posix.dumps(1)
    return filter(lambda s: 'flag{' in s, out.split())[0]
    
#    sm.run()

    # Get the stdout of every path that reached an exit syscall. The flag should be in one of these!
#    out = ''
#    for pp in sm.deadended:
#        out = pp.posix.dumps(1)
#        if 'flag{' in out:
#            return filter(lambda s: 'flag{' in s, out.split())[0]

    # Runs in about 15 minutes!

def test():
    assert main() == 'flag{dr4g0n_or_p4tric1an_it5_LLVM}'

if __name__ == "__main__":
    before = time.time()
    print main()
    after = time.time()
    print "Time elapsed: {}".format(after - before)
