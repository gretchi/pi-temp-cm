#!/bin/bash

SCRIPT_DIR=$(cd $(dirname $0) && pwd)

LIB_PATH="lib-common"
LINK_TO_1_PATH="controller/cm-daemon"
LINK_TO_2_PATH="driver/admin-daemon"

DEFAULT_IFS=$IFS
IFS=$'\n'

# remove link
cd "${SCRIPT_DIR}"
DEFAULT_IFS=$IFS
IFS=$'\n'

for link_to_dir in `echo -e "${LINK_TO_1_PATH}\n${LINK_TO_2_PATH}"`; do
    for line in $(ls "${link_to_dir}"); do
        IFS=$DEFAULT_IFS
        target_path="${link_to_dir}/${line}"

        if [ -d "${target_path}" ]; then
            if [ -L "${target_path}" ]; then
                # do
                echo unlink "${target_path}"
                unlink "${target_path}"
            fi
        fi
    done
done


# link
cd "${SCRIPT_DIR}"
DEFAULT_IFS=$IFS
IFS=$'\n'
for line in $(ls "${LIB_PATH}"); do
    IFS=$DEFAULT_IFS
    target_path="${LIB_PATH}/${line}"

    if [ -d ${target_path} ]; then
        cd "${LINK_TO_1_PATH}"
        ln -s "../../${LIB_PATH}/${line}" "${line}"
        cd "${SCRIPT_DIR}"

        cd "${LINK_TO_2_PATH}"
        ln -s "../../${LIB_PATH}/${line}" "${line}"
        cd "${SCRIPT_DIR}"
    fi
done
