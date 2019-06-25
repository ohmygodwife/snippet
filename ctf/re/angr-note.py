#workon angr
import angr
import logging
#detail log
logging.getLogger('angr').setLevel('DEBUG')
#brief log
logging.basicConfig()
angr.manager.l.setLevel('DEBUG')
logging.getLogger('angr.manager').setLevel(logging.DEBUG)

proj = angr.Project('./baby-re',  load_options={'auto_load_libs': False})
proj.hook(0x4018B0, angr.SIM_PROCEDURES['glibc']['__libc_start_main']())
strlen = lambda state, arguments: \
        angr.SIM_PROCEDURES['libc']['strlen'](proj).execute(
            state, arguments=arguments
        )
flag_length_bvs = strlen(found, arguments=[flag_addr]).ret_expr #ret_expr to get return bvs from SimProcedure object

hex(proj.entry)

proj.loader.shared_objects
proj.loader.all_elf_objects  #windows program we'd use all_pe_objects!
proj.loader.main_object
proj.loader.find_object_containing(0x400000) #get a reference to an object given an address in it
malloc = proj.loader.find_symbol('malloc')
malloc.rebased_addr  #address in the global address space.
malloc.linked_addr   #relative to the prelinked base of the binary.
malloc.relative_addr #relative to the object base.
# On Loader, the method is find_symbol because it performs a search operation to find the symbol.
# On an individual object, the method is get_symbol because there can only be one symbol with a given name.
main_malloc = proj.loader.main_object.get_symbol("malloc")

block = proj.factory.block(proj.entry)
block.pp()                          # pretty-print a disassembly to stdout
block.instructions                  # how many instructions are there?
block.instruction_addrs             # what are the addresses of the instructions?

# In order to do this peformantly, we will use the unicorn engine!
st = p.factory.entry_state(add_options=angr.options.unicorn)
# By default, all symbolic write indices are concretized.
state = proj.factory.entry_state(add_options={"SYMBOLIC_WRITE_ADDRESSES"})
state = proj.factory.entry_state()  #.call_state(addr, arg1, arg2, ...), where addr is the address of the function you want to call and argN is the Nth argument to that function, If you want to have memory allocated and actually pass in a pointer to an object, you should wrap it in an PointerWrapper, angr.PointerWrapper('\0'*100)
if (state.ip.args[0] == addrStrcpy):    # Just check p.state.ip.args[0] (the current instruction pointer)
state.regs.rip
state.regs.rax
# mem[index].type (common values: char, short, int, long, size_t, uint8_t, uint16_t...)
# Use .resolved to get the value as a bitvector Use .concrete to get the value as a python int
state.mem[proj.entry].int.resolved  # interpret the memory at the entry point as a C int as a bitvector
bv = state.solver.BVV(0x1234, 32)       # create a 32-bit-wide bitvector with value 0x1234, BVV stands for bitvector value
state.solver.eval(bv)                # convert to python int
x = state.solver.BVS("x", 64) #bitvector symbol named "x" of length 64 bits
one_hundred > -5 #comparisons are unsigned by default. The -5 is coerced to <BV64 0xfffffffffffffffb>
one_hundred.SGT(-5) #that's "signed greater-than"
yes = one == 1
state.solver.is_true(yes)  #True
a = state.solver.FPV(3.2, state.solver.fp.FSORT_DOUBLE)
b = state.solver.FPS('b', state.solver.fp.FSORT_DOUBLE)
a.raw_to_bv()   #fp to bv
state.solver.BVS('x', 64).raw_to_fp() #bv to fp
a.val_to_bv(12)
a.val_to_bv(12).val_to_fp(state.solver.fp.FSORT_FLOAT)

state.regs.rsi = state.solver.BVV(3, 64)  # set register
state.mem[0x1000].long = 4                # set memory
state.regs.rbp = state.mem[state.regs.rbp].uint64_t.resolved

for addr in state.history.bbl_addrs:
  print hex(addr)
succ = state.step()  #perform one step of symbolic execution and return an object called SimSuccessors
len(succ.successors) == 2:
  break
state1, state2 = succ.successors
input_data = state1.posix.files[0].all_bytes() #retrieve a bitvector represnting all the content read from stdin(files[0]) so far.
state1.solver.eval(input_data, cast_to=str)

files = {'/dev/stdin': angr.storage.file.SimFile("/dev/stdin", "r", size=30)}
# set SimFile from asisctffinals2015_license.py
bytes = state.solver.Concat(bytes, state.solver.BVV(0x0a, 8), *line)
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


s = proj.factory.entry_state(fs=files, concrete_fs=True, chroot="angr-chroot/") #if the program you are analyzing attempts to open '/etc/passwd', you can set the chroot to your current working directory so that attempts to access '/etc/passwd' will read from '$CWD/etc/passwd'.

# Constrain the first 8 bytes to be non-null and non-newline:
for _ in xrange(8):
  k = state.posix.files[0].read_from(1)
  state.se.add(k >= 32)
  state.se.add(k < 127)

# Constrain the last byte to be a newline
k = state.posix.files[0].read_from(1)
state.se.add(k == 10)

# Reset the symbolic stdin's properties and set its length.
state.posix.files[0].seek(0)
state.posix.files[0].length = 9

# Set memory directly
bvs = state.solver.BVS('toMemory', 8*4)
state.se.add(bvs > 1000)
state.memory.store(0x08049b80, bvs.reversed)

simgr = proj.factory.simgr(state)
while len(simgr.active) == 1:
  simgr.step()  # both of the successor states appear in the stash, and you can step both of them in sync. 
simgr.run()     # Step until everything terminates
simgr.explore(find=lambda s: "Congrats" in s.posix.dumps(1))
s = simgr.found[0]
print s.posix.dumps(1)
flag = s.posix.dumps(0)
print(flag)
simgr.active[0].regs.rip                 # new and exciting!
state.regs.rip                           # still the same!

class SearchForNull(angr.ExplorationTechnique):
    def setup(self, simgr):
        if 'found' not in simgr.stashes:
            simgr.stashes['found'] = []

    def filter(self, state):
        if state.addr == 0:
            return 'found'
        return None

    def complete(self, simgr):
        return len(simgr.found)
        
simgr.use_technique(SearchForNull())
simgr.run()
#NOTICE: be careful when applying tech = angr.exploration_techniques.Explorer(find = lambda s:s.addr == 0) with other techniques, since Explorer def step, which would call manager.step while hooking step!!!!!!! Should NOT def step in subclass of ExplorationTechnique, otherwise would case manager.step run one more time!!!!! So explore technique should not use with other technique!!!!

#break point
def track_reads(state):
  print 'Read', state.inspect.mem_read_expr, 'from', state.inspect.mem_read_address
state.inspect.b('mem_read', when=angr.BP_AFTER, action=track_reads)
state.inspect.b('instruction', when=angr.BP_AFTER, instruction=0x8000, mem_read_expr=0x1000) #This will break after instruction 0x8000, but only 0x1000 is a possible value of the last expression that was read from memory

def find_input():
  state = proj.factory.entry_state()
  input = state.solver.BVS('input', 64)
  operation = (((input + 4) * 3) >> 1) + input
  output = 200
  state.solver.add(operation == output) #could add more constraints
  state.satisfiable()       #True
  state.solver.eval(input)  #0x3333333333333381
  #solver.eval(expression) will give you one possible solution to the given expression.
  #solver.eval_one(expression) will give you the solution to the given expression, or throw an error if more than one solution is possible.
  #solver.eval_upto(expression, n) will give you up to n solutions to the given expression, returning fewer than n if fewer than n are possible.
  #solver.eval_atleast(expression, n) will give you n solutions to the given expression, throwing an error if fewer than n are possible.
  #solver.eval_exact(expression, n) will give you n solutions to the given expression, throwing an error if fewer or more than are possible.
  #solver.min(expression) will give you the minimum possible solution to the given expression.
  #solver.max(expression) will give you the maximum possible solution to the given expression.

def main():
  proj = angr.Project('./baby-re',  load_options={'auto_load_libs': False})
  path_group = proj.factory.path_group(threads=4) # 设置了四个线程，对于这个程序线程再多了没意义
  # 如果是0x40294b就执行，如果是0x402941就不去执行
  path_group.explore(find=0x40294b, avoid=0x402941)
  # flag在0x40292c的位置
  print path_group.found[0].state.posix.dumps(0)
  return path_group.found[0].state.posix.dumps(1) # dumps出flag

if __name__ == '__main__':
  print(repr(main()))