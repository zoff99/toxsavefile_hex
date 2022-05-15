#! /bin/bash

_HOME2_=$(dirname $0)
export _HOME2_
_HOME_=$(cd $_HOME2_;pwd)
export _HOME_

echo $_HOME_
cd $_HOME_

if [ "$1""x" == "buildx" ]; then
    docker build -t toxsavefile_analyser .
elif [ "$1""x" == "manualx" ]; then
    docker run -ti --rm \
    -v "$_HOME_":/workspace \
    toxsavefile_analyser \
    /bin/sh -c "apk add bash >/dev/null 2>/dev/null; cd /workspace/ ; /bin/bash "
elif [ "$1""x" == "kscx" ]; then
    docker run -ti --rm \
    -v "$_HOME_":/workspace \
    toxsavefile_analyser \
    /bin/sh -c "apk add bash >/dev/null 2>/dev/null; cd /workspace/ ; /usr/local/kaitai-struct-compiler-0.9/bin/kaitai-struct-compiler tox_save.ksy --target python "
elif [ "$1""x" == "insidex" ]; then
    echo "== now inside docker =="
    cd /workspace/ || exit 1
    if [ ! -e ./tox_save.tox ]; then
        echo "== tox_save.tox file not found =="
        exit 2
    elif [ ! -s ./tox_save.tox ]; then
        echo "== tox_save.tox file has 0 byte size =="
        exit 3
    else
        python3 ./tox_save_extract.py
        res=$?
        chmod -R a+rw ./__pycache__
        chmod a+rw ./tox_save.groups.dat
        exit $res
    fi
else
    docker run -ti --rm \
    -v "$_HOME_":/workspace \
    toxsavefile_analyser \
    /bin/sh -c "apk add bash >/dev/null 2>/dev/null; /bin/bash /workspace/run.sh inside"
fi
