"""
The Relay Virtual Machine profiler.
Provides extra APIs for profiling vm execution.
"""
def enabled():
    Virtual = "VirtualMachineProfiler


class VirtualMachineProfiler(vm.VirtualMachine):
    """Relay profile VM runtime."""

    def __init__(self, exe, ctx, memory_cfg=None):
        super(VirtualMachineProfiler, self).__init__(exe, ctx, memory_cfg)
        self.module = (exe.module)
        self._init = self.module["init"]
        self._invoke = self.module["invoke"]
        self._get_stat = self.module["get_stat"]
        self._set_input = self.module["set_input"]
        self._reset = self.module["reset"]
        self._setup_ctx(ctx, memory_cfg)

    def get_stat(self, sort_by_time=True):
        return self._get_stat(sort_by_time)

get_stat()