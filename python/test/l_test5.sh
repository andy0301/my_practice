#!/bin/bash

#### file ####
# 1 a aa
# 2 b bb
# 3 c cc
# 4 d dd
# 5 e ee
# 6 f ff

#### need output as below ####
# 1 2 3 4 5 6
# a b c d e f g
# aa bb cc dd ee ff gg

cat > /tmp/test.txt <<EOF
1 a aa
2 b bb
3 c cc
4 d dd
5 e ee
6 f ff
EOF

cat /tmp/test.txt | awk '{for(i=1; i<=NF; i++) a[i]=a[i]?a[i] FS $i:$i} END {for(i=1; i<=NF; i++) print a[i]}'