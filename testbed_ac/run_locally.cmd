@echo off
:: load in the settings.env variables
for /f "delims== tokens=1,2" %%G in (settings.env) do set %%G=%%H
for /f "delims=: tokens=1,2" %%G in ('python -m pip show asistagenthelper-pkg-rcarff-ihmc') do set %%G=%%H
set AGENT_HELPER_VERSION=%Version%

cd src
python %AGENT_MAIN_RUN_FILE%
