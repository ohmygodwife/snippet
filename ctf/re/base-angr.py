# re_find_plut0, 210813inctf
import angr
import claripy
import sys
import logging
#detail log
#logging.getLogger('angr').setLevel('DEBUG')
#brief log
#angr.manager.l.setLevel('DEBUG')

#logging.basicConfig()
#logging.getLogger('angr.manager').setLevel(logging.DEBUG)

proj = angr.Project("./re_find_plut0", load_options={'auto_load_libs': False})

base = 0x400000

def add_cond(state, argv1):
  for byte in argv1.chop(8):
#        state.add_constraints(byte != '\x00') # null
    # '\0' || '\x20' - '\x7e'
    cond = state.solver.Or(
            byte == '\0', 
            state.solver.And(
               byte >= 0x20, byte < 0x7f))
    state.add_constraints(cond)

def argv(): #variable passed by argv
  argv1 = claripy.BVS("argv1",100*8)
  state = proj.factory.entry_state(args=["",argv1])
#  add_cond(state, argv1)
  simgr = proj.factory.simgr(state)
  simgr.explore(find=0x400A84, avoid=[0x400A90])
#  simgr.explore(find=lambda s:"correct!" in s.posix.dumps(1))
  print(simgr.one_found.solver.eval(argv1, cast_to=str))

def hook(): #variable passed by hooked scanf
  flag = claripy.BVS("flag",100*8)
  state = proj.factory.entry_state(add_options=angr.options.unicorn)
#  add_cond(state, flag) #add_cond is slower than not, do not know why
  
  class my_scanf_for_s(angr.SimProcedure):
    def run(self, fmt, ptr):
      self.state.memory.store(ptr, flag)
  proj.hook_symbol('__isoc99_scanf', my_scanf_for_s(), replace=True)
  
  simgr = proj.factory.simgr(state)
  simgr.explore(find=0x400A84, avoid=[0x400A90])
  simgr.explore(find=lambda s:"correct!" in s.posix.dumps(1))
  print(simgr.one_found.solver.eval(flag, cast_to = str))

def stdin(): #variable passed by stdin
  passwd_len = int(sys.argv[1])
  
  #with unicorn 54sec, without 58sec
#  state = proj.factory.entry_state(add_options=angr.options.unicorn)
  
  flag_chars = [claripy.BVS('flag_%d' % i, 8) for i in range(passwd_len)]
  flag = claripy.Concat(*flag_chars + [claripy.BVV(b'\n')])
  
  state = proj.factory.full_init_state(
        args=[],
        add_options=angr.options.unicorn,
        stdin=flag,
    )
    
  # Constrain the first 28 bytes to be non-null and non-newline:
  for k in flag_chars:
    state.solver.add(k >= 0x20)
    state.solver.add(k < 0x7f)
  
  simgr = proj.factory.simgr(state)
#  simgr.explore(find=lambda s:"correct!" in s.posix.dumps(1))
  simgr.explore(find=base + 0xadb, avoid=[base + 0x8aa])
  print(simgr.one_found.posix.dumps(0))
  print(simgr.one_found.posix.dumps(1))

def test():
    assert stdin() == 'ais3{I_tak3_g00d_n0t3s}'

if  __name__=="__main__":
  stdin()
#  hook() #hook is slower than stdin