import psutil

print("Cpu的逻辑数量...%d"%psutil.cpu_count())
print("Cpu的物理核心...%d"%psutil.cpu_count(logical=False))
print("Cpu系统时间...",psutil.cpu_times())

for x in range(10):
    print(psutil.cpu_percent(interval=1,percpu=True))
print('电脑虚拟内存',psutil.virtual_memory())
print('电脑实际内村',psutil.swap_memory())

print('磁盘分区：',psutil.disk_partitions())
print('磁盘使用情况：',psutil.disk_usage('/'))
print('磁盘的I\O能力：。。',psutil.disk_io_counters())


print('磁盘的I\O读写能力：。。',psutil.net_io_counters())

print('获取网络接口：....',psutil.net_if_addrs())
print('获取网络状态：....',psutil.net_if_stats())
print('获取网络信息：....',psutil.net_connections())

print('获取进口ID：....',psutil.pids())
p = psutil.Process(3776)
print('获取进口名称：....',p.name())
print('获取进口工作表：....',p.cwd())






