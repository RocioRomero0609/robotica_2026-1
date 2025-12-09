import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/rocioromero/robotica_2026-1/install/nodes_topics_py'
