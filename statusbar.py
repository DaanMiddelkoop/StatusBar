from time import sleep
from TimeModule import Time
from cpu_module import CpuModule, OwnCpuUsage, cpu
from memory_module import MemoryModule
from disk_space_free_module import DiskSpaceFreeModule
from quote_module import QuoteModule
import psutil


def main():
    print('{ "version": 1 }')
    print('[')
    print('[]')

    modules = list()
    modules.append(QuoteModule())
    modules.append(DiskSpaceFreeModule())
    modules.append(MemoryModule())
    modules.append(OwnCpuUsage())
    for i in range(0, len(psutil.cpu_percent(percpu=True))):
        modules.append(CpuModule(i))
    modules.append(Time())

    while True:

        cpu.refresh_cpu()
        print(',[')

        for module in modules:
            print(module.output())
            print(',')

        print('{"full_text":""}]')

        sleep(1)


main()
