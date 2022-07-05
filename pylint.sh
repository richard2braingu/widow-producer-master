#!/bin/bash

source venv/bin/activate
# pylint does not lint c extensions (like `lxml`) correctly, so it MUST be added as extra switch
export PYLINT_EXTRA_SWITCHES=-"-disable=duplicate-code --extension-pkg-allow-list=lxml"
export PYLINT_EXCLUSIONS="venv|.cache"
find . -type f -iname "*.py" | grep -vE "${PYLINT_EXCLUSIONS}" > /tmp/pylint_files.txt
cat /tmp/pylint_files.txt
python -m pylint ${PYLINT_EXTRA_SWITCHES} $(< /tmp/pylint_files.txt)