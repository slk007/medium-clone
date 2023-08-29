#!/usr/bin/env bash

yes_no(){
  declare desc="Prompt for confirmation. \$\"\{1\}\": confirmation message"

  local args1="${1}"

  local response=read -r -p "${args1} (y/[n]) " response

  if [[ "${response}" =~ ^[Yy]$ ]]
  then
    exit 0
  else
    exit 1
  fi
}