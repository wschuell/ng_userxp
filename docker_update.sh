#!/bin/bash


docker exec -it ng /bin/bash << 'EOF'

bash update.sh
exit

EOF

git pull