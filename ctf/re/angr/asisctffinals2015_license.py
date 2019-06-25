import angr

def main():
    p = angr.Project("asisctffinals2015_license", load_options={'auto_load_libs': False})

    # Create a blank state
    state = p.factory.blank_state()

    # Build the file whose name is weird
    license_name = "_a\nb\tc_"

    # 96: if ( -45235 * v6 * v6 * v6 * v6
    #       + -1256 * v6 * v6 * v6
    #       + 14392 * v6 * v6
    #       + -59762 * v6
    #       - 1949670109068LL
    #       + 44242 * v6 * v6 * v6 * v6 * v6 )  -> bruteforce get v6 = 34
    # 130: else if ( v12 == 5 )   -> 4 '0x0a'
    # This is the license file
    # From analyzing the binary, we know that the license file should have five 
    # lines in total, and each line has 6 characters. Not setting file content 
    # may also work, but in that case, angr will produce many more paths, and we 
    # will spent much more time in path trimming.

    bytes = None
    constraints = [ ]
    for i in xrange(5):
        line = [ ]
        for j in xrange(6):
            line.append(state.solver.BVS('license_file_byte_%d_%d' % (i, j), 8))
            state.add_constraints(line[-1] != 0x0a)
        if bytes is None:
            bytes = state.solver.Concat(*line)
        else:
            bytes = state.solver.Concat(bytes, state.solver.BVV(0x0a, 8), *line)
#    bytes = state.solver.BVS('bytes', 34 * 8)
    content = angr.state_plugins.SimSymbolicMemory(memory_id="file_%s" % license_name)
    content.set_state(state)
    content.store(0, bytes)

    license_file = angr.storage.SimFile(license_name, 'rw', content=content, size=len(bytes) / 8)

    # Build the file system dict
    # This interface might change in the near future
    fs = {
        license_name: license_file
    }
    state.posix.fs = fs

    ex = p.surveyors.Explorer(
                            start=state,
                            find=(0x400e93, ),
                            avoid=(0x400bb1, 0x400b8f, 0x400b6d, 0x400a85,
                                   0x400ebf, 0x400a59)
                            )
    ex.run()

    # One path will be found
    found = ex.found[0]
    print hex(found.solver.eval(bytes))
    rsp = found.regs.rsp
    #.text:0000000000400EA2                 lea     rsi, [rsp+278h+var_D8]
    flag_addr = rsp + 0x278 - 0xd8 # Ripped from IDA 
#    '''
    # Perform an inline call to strlen() in order to determine the length of the 
    # flag
    FAKE_ADDR = 0x100000
    strlen = lambda state, arguments: \
        angr.SIM_PROCEDURES['libc']['strlen'](p, FAKE_ADDR, p.arch).execute(
            state, arguments=arguments
        )
    flag_length = strlen(found, arguments=[flag_addr]).ret_expr
    # In case it's not null-terminated, we get the least number as the length
    flag_length_int = min(found.solver.eval_upto(flag_length, 3))
    # Read out the flag!
    flag_int = found.solver.eval(found.memory.load(flag_addr, flag_length_int))
    flag = hex(flag_int)[2:-1].decode("hex")
#    '''
#    flag = found.solver.eval(found.memory.load(flag_addr, 100), cast_to=str)
    return flag

def test():
    assert main() == 'ASIS{8d2cc30143831881f94cb05dcf0b83e0}'

if __name__ == '__main__':
    print main()

