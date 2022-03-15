#!/usr/bin/env bash

set -u

function set_ucf_git() {
  pushd . >>/dev/null
  my_dir=$(dirname $0)
  cd $my_dir
  cd ..
  ucf_git=$PWD
  popd >/dev/null
}
set_ucf_git

echo "Testbed is checked out at: $asist_testbed"
tb_ac=${asist_testbed}/Agents/AC_UCF_TA2_PlayerProfiler
echo "ucf git $ucf_git"

echo "Updating config.json"
cp -a $ucf_git/ConfigFolder/config.json ${tb_ac}/ConfigFolder/config.json

echo "Updating settings.env"
cp -a $ucf_git/settings.env ${tb_ac/settings.env/}

echo "Updating Launcher file"
cp -a $ucf_git/docker-compose.launcher.yml ${tb_ac/docker-compose.launcher.yml/}
